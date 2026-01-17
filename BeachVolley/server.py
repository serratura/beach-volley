import asyncio
import json
import tornado.ioloop
import tornado.web
import tornado.websocket
import sys
import os
from pymongo import AsyncMongoClient

if sys.platform.startswith("win"):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

#  variabili globali per db, clients e fattori per il torneo
mongo_client = AsyncMongoClient("localhost", 27017)
db = mongo_client["beachvolley"]
clients = set()
secondi_simulati = 45
live_matches = []
current_phase = "Ottavi di Finale"
TOURNAMENT_NAME = "Tappa 2 Assoluti"


#  funzioni db
async def get_ranking():
    teams_cursor = db.teams.find().sort("points", -1)
    teams = await teams_cursor.to_list(length=16)
    for team in teams:
        if "_id" in team:
            team["_id"] = str(team["_id"])
    return teams


async def award_points(team_name, points):
    await db.teams.update_one({"name": team_name}, {"$inc": {"points": points}})


async def carica_match_in_archivio(match):
    try:
        match_data = json.loads(json.dumps(match, default=str))
        await db.tournaments.update_one(
            {"name": TOURNAMENT_NAME},
            {"$push": {f"partite.{current_phase}": match_data}}
        )
        print(f"✅ ARCHIVIO: Salvato {match['teamA']} vs {match['teamB']} ({current_phase})")
    except Exception as e:
        print(f"❌ ERRORE ARCHIVIO: {e}")


# funzioni logica torneo

async def init_matches():
    global live_matches, current_phase
    await db.tournaments.update_one(
        {"name": TOURNAMENT_NAME},
        {"$set": {"partite": {"Ottavi di Finale": [], "Quarti di Finale": [], "Semifinali": [], "Finali": []}}}
    )

    teams = await db.teams.find().sort("points", -1).to_list(length=16)
    accoppiamenti = [(0, 15), (7, 8), (3, 12), (4, 11), (1, 14), (6, 9), (2, 13), (5, 10)]
    live_matches = []
    current_phase = "Ottavi di Finale"

    for i in range(len(accoppiamenti)):
        id_a, id_b = accoppiamenti[i]
        team_a = teams[id_a]
        team_b = teams[id_b]
        nuovo_match = crea_oggetto_match(i + 1, team_a["name"], team_b["name"])
        live_matches.append(nuovo_match)
    print(f"{TOURNAMENT_NAME} Iniziata!")

#  logica torneo


def crea_oggetto_match(m_id, teamA, teamB, final_type=None):
    return {
        "id": m_id,
        "teamA": teamA,
        "teamB": teamB,
        "playersA": teamA.split(" - "),
        "playersB": teamB.split(" - "),
        "score_sets": [0, 0],
        "current_set": 0,
        "points": [0, 0],
        "sets_history": [],
        "events": [],
        "match_time": 0,
        "status": "live",
        "server_team": 0,
        "server_index": [0, 0],
        "final_type": final_type
    }


def get_winner(m):
    return {"name": m["teamA"]} if m["score_sets"][0] > m["score_sets"][1] else {"name": m["teamB"]}


def get_loser(m):
    return {"name": m["teamA"]} if m["score_sets"][0] < m["score_sets"][1] else {"name": m["teamB"]}


def start_next_phase():
    global live_matches, current_phase
    winners = [get_winner(m) for m in live_matches]
    losers = [get_loser(m) for m in live_matches]

    if current_phase == "Ottavi di Finale":
        current_phase = "Quarti di Finale"
        live_matches = [crea_oggetto_match(i + 1, winners[i * 2]["name"], winners[i * 2 + 1]["name"]) for i in range(4)]
    elif current_phase == "Quarti di Finale":
        current_phase = "Semifinali"
        live_matches = [crea_oggetto_match(i + 1, winners[i * 2]["name"], winners[i * 2 + 1]["name"]) for i in range(2)]
    elif current_phase == "Semifinali":
        current_phase = "Finali"
        live_matches = [
            crea_oggetto_match(1, losers[0]["name"], losers[1]["name"], "3-4"),
            crea_oggetto_match(2, winners[0]["name"], winners[1]["name"], "1-2")]
    else:
        current_phase = "Torneo Completato"
        live_matches = []
    print(f"✨ Passaggio a: {current_phase}")


# timer

async def match_timer():
    while True:
        wait_time = 60.0 / secondi_simulati
        await asyncio.sleep(wait_time)
        for m in live_matches:
            if m["status"] == "live":
                m["match_time"] += 60

#  logica punti


async def apply_point(match, scoring_team):
    a, b = match["points"]
    if scoring_team == 0:
        a += 1
    else:
        b += 1
    match["points"] = [a, b]

    match["events"].append({
        "match_time": match["match_time"],
        "description": f"Punto Team {'A' if scoring_team == 0 else 'B'} ({a}-{b})",
        "score": f"{a}-{b}"
    })

    frequenza_cambio = 7 if match["current_set"] < 2 else 5
    if (a + b) % frequenza_cambio == 0 and (a + b) != 0:
        match["events"].append({
            "match_time": match["match_time"],
            "description": "🔄 Cambio Campo",
            "type": "Info"
        })

    if match["current_set"] < 2 and (a + b) == 21:
        match["events"].append({
            "match_time": match["match_time"],
            "description": "⏸ Time-out Tecnico",
            "type": "Info"
        })

    target = 21 if match["current_set"] < 2 else 15
    if (a >= target or b >= target) and abs(a - b) >= 2:
        winner_id = 0 if a > b else 1
        match["sets_history"].append([a, b])
        match["score_sets"][winner_id] += 1

        match["events"].append({
            "match_time": match["match_time"],
            "description": f"🏐 Fine Set {match['current_set'] + 1} - Vinto da {'A' if winner_id == 0 else 'B'}",
            "type": "Fine Set"
        })

        match["points"] = [0, 0]
        match["current_set"] += 1

        if match["score_sets"][winner_id] == 2 or match["current_set"] == 3:
            match["status"] = "finished"
            match["events"].append({
                "match_time": match["match_time"],
                "description": "🏁 Partita Terminata",
                "type": "Fine Match"
            })
            await carica_match_in_archivio(match)

            winner_name = match["teamA"] if winner_id == 0 else match["teamB"]
            await award_points(winner_name, 20)

            tutti_finiti = True
            for m in live_matches:
                if m["status"] == "live":
                    tutti_finiti = False
                    break

            if tutti_finiti == True:
                start_next_phase()


# handlers

async def ws_broadcaster():
    while True:
        if clients:
            rank = await get_ranking()
            msg = json.dumps({
                "type": "match_update",
                "tournament_name": TOURNAMENT_NAME,
                "matches": live_matches,
                "phase": current_phase,
                "ranking": rank
            })
            for c in list(clients):
                try:
                    await c.write_message(msg)
                except:
                    clients.discard(c)
        await asyncio.sleep(1)


class WSHandler(tornado.websocket.WebSocketHandler):
    def open(self): clients.add(self)

    def on_close(self): clients.discard(self)

    def check_origin(self, origin): return True


class PointReceiverHandler(tornado.websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True

    async def on_message(self, message):
        data = json.loads(message)
        m_id, team_id = int(data.get("match_id")), (0 if data.get("team") == "A" else 1)
        for m in live_matches:
            if m["id"] == m_id and m["status"] == "live":
                await apply_point(m, team_id)
                break


class MainHandler(tornado.web.RequestHandler):
    def get(self): self.render("index.html")


class MatchHandler(tornado.web.RequestHandler):
    def get(self, match_id): self.render("match.html", match_id=match_id)


class ArchiveAPIHandler(tornado.web.RequestHandler):
    async def get(self):
        cursor = db.tournaments.find().sort("_id", -1)
        tornei = await cursor.to_list(100)
        for t in tornei:
            t["_id"] = str(t["_id"])
        self.write(json.dumps(tornei))


class ArchiveHtmlHandler(tornado.web.RequestHandler):
    def get(self): self.render("archivio.html")


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler), (r"/match/(\d+)", MatchHandler),
        (r"/ws", WSHandler), (r"/points", PointReceiverHandler),
        (r"/api/archive", ArchiveAPIHandler), (r"/archivio", ArchiveHtmlHandler),
    ], template_path="templates", debug=True)


async def main():
    await init_matches()
    make_app().listen(8888)
    print("http://localhost:8888")
    await asyncio.gather(ws_broadcaster(), match_timer())


if __name__ == "__main__":
    asyncio.run(main())