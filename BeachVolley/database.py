import asyncio
import json
import os
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId


async def init_database():
    # In Docker usiamo 'db', in locale 'localhost'
    mongo_url = os.environ.get("MONGO_URL", "mongodb://db:27017")
    client = AsyncIOMotorClient(mongo_url)
    db = client["beachvolley"]

    tappa_esistente = None

    # Proviamo prima a vedere se esiste il file JSON (backup)
    if os.path.exists("tappa_1.json"):
        with open("tappa_1.json", "r", encoding="utf-8") as f:
            tappa_esistente = json.load(f)
            # Rimuoviamo l'ID stringa per evitare conflitti al nuovo inserimento
            if "_id" in tappa_esistente:
                del tappa_esistente["_id"]
            print("Tappa 1 caricata da file tappa_1.json")
    else:
        # Se non c'è il file, cerchiamo nel DB attuale
        tappa_db = await db.tournaments.find_one({"name": "Tappa 1 Assoluti"})
        if tappa_db:
            tappa_esistente = tappa_db
            if "_id" in tappa_esistente:
                del tappa_esistente["_id"]
            print("Tappa 1 recuperata dal database attuale")
        else:
            print("Tappa 1 non trovata, ne creerò una vuota.")
            tappa_esistente = {
                "name": "Tappa 1 Assoluti",
                "played": True,
                "partite": {"Ottavi di Finale": [], "Quarti di Finale": [], "Semifinali": [], "Finali": []}
            }

    await db.teams.delete_many({})
    await db.tournaments.delete_many({})

    teams = [
        "ALFIERI MANUEL - RANGHIERI ALEX", "ANDREATTA TIZIANO - BENZI DAVIDE",
        "COTTAFAVA SAMUELE - DAL CORSO GIANLUCA", "PODESTA' SIMONE - MARTINO MATTEO",
        "MARCHETTO TOBIA - DAL MOLIN DAVIDE", "BONIFAZI CARLO - ACERBI RAOUL",
        "SACRIPANTI MAURO - TITTA GIACOMO", "SPADONI GIACOMO - LUISETTO MICHELE",
        "LUPO DANIELE - BORRACCINO DAVIDE", "KRUMINS DAVIS - CAMINATI MARCO",
        "CECCOLI EDGARDO - CARUCCI ALESSANDRO", "GEROMIN FEDERICO - CAMOZZI MATTEO",
        "AREZZO DI TRIFILETTI FRANCO - BIGARELLI LUCA", "VISCOVICH MARCO - ROSSI ENRICO",
        "PIZZILEO FILIPPO - INGROSSO PAOLO", "PRETI ALESSANDRO - MUSSA FABRIZIO"
    ]
    punti = [400, 504, 300, 200, 300, 600, 700, 500, 900, 1200, 600, 700, 600, 200, 500, 400]

    team_data = [{"name": teams[i], "points": punti[i]} for i in range(len(teams))]
    await db.teams.insert_many(team_data)

    tappa2 = {
        "name": "Tappa 2 Assoluti",
        "played": False,
        "partite": {"Ottavi di Finale": [], "Quarti di Finale": [], "Semifinali": [], "Finali": []}
    }

    await db.tournaments.insert_many([tappa_esistente, tappa2])

    backup_tappa1 = tappa_esistente.copy()
    with open("tappa_1.json", "w", encoding="utf-8") as f:
        json.dump(backup_tappa1, f, indent=4, ensure_ascii=False)

    print("✅ Database inizializzato correttamente con Tappa 1 e Tappa 2.")
    client.close()


if __name__ == "__main__":
    asyncio.run(init_database())