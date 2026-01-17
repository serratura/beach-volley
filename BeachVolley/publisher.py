import asyncio
import json
import os
from pymongo import AsyncMongoClient


async def init_database():
    # In Docker l'host è 'db', in locale è 'localhost'
    mongo_url = os.environ.get("MONGO_URL", "mongodb://db:27017")
    client = AsyncMongoClient(mongo_url)
    db = client["beachvolley"]

    print("Inizializzazione Database in corso...")

    tappa1 = None
    if os.path.exists("tappa_1_clean.json"):
        with open("tappa_1_clean.json", "r", encoding="utf-8") as f:
            tappa1 = json.load(f)
            # Per sicurezza, se l'id fosse sfuggito, lo cancelliamo qui
            tappa1.pop("_id", None)
            print("✅ Tappa 1 caricata dal file pulito.")
    else:
        tappa1 = {
            "name": "Tappa 1 Assoluti",
            "played": True,
            "partite": {"Ottavi di Finale": [], "Quarti di Finale": [], "Semifinali": [], "Finali": []}
        }

    await db.teams.delete_many({})
    await db.tournaments.delete_many({})

    teams = ["ALFIERI MANUEL - RANGHIERI ALEX", "ANDREATTA TIZIANO - BENZI DAVIDE",
             "COTTAFAVA SAMUELE - DAL CORSO GIANLUCA", "PODESTA' SIMONE - MARTINO MATTEO",
             "MARCHETTO TOBIA - DAL MOLIN DAVIDE", "BONIFAZI CARLO - ACERBI RAOUL", "SACRIPANTI MAURO - TITTA GIACOMO",
             "SPADONI GIACOMO - LUISETTO MICHELE", "LUPO DANIELE - BORRACCINO DAVIDE", "KRUMINS DAVIS - CAMINATI MARCO",
             "CECCOLI EDGARDO - CARUCCI ALESSANDRO", "GEROMIN FEDERICO - CAMOZZI MATTEO",
             "AREZZO DI TRIFILETTI FRANCO - BIGARELLI LUCA", "VISCOVICH MARCO - ROSSI ENRICO",
             "PIZZILEO FILIPPO - INGROSSO PAOLO", "PRETI ALESSANDRO - MUSSA FABRIZIO"]
    punti = [400, 504, 300, 200, 300, 600, 700, 500, 900, 1200, 600, 700, 600, 200, 500, 400]

    docs_teams = []

    for i in range(len(teams)):
        documento = {
            "name": teams[i],
            "points": punti[i]
        }
        docs_teams.append(documento)
    await db.teams.insert_many(docs_teams)


    tappa2 = {
        "name": "Tappa 2 Assoluti",
        "played": False,
        "partite": {"Ottavi di Finale": [], "Quarti di Finale": [], "Semifinali": [], "Finali": []}
    }

    await db.tournaments.insert_many([tappa1, tappa2])

    print("✨ Database pronto con ID rigenerati automaticamente!")
    client.close()


if __name__ == "__main__":
    asyncio.run(init_database())