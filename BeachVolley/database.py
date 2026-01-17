import asyncio
from pymongo import AsyncMongoClient
import os

async def init_database():
    mongo_url = os.environ.get("MONGO_URL", "mongodb://localhost:27017")
    client = AsyncMongoClient(mongo_url)
    db = client["beachvolley"]

    tappa_esistente = await db.tournaments.find_one({"name": "Tappa 1 Assoluti"})

    if not tappa_esistente:
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

    for i in range(len(teams)):
        await db.teams.insert_one({"name": teams[i], "points": punti[i]})
    tappa2 = {
        "name": "Tappa 2 Assoluti",
        "played": False,
        "partite": {"Ottavi di Finale": [], "Quarti di Finale": [], "Semifinali": [], "Finali": []}
    }
    if "_id" in tappa_esistente:
        del tappa_esistente["_id"]

    await db.tournaments.insert_many([tappa_esistente, tappa2])
    print("Database inizializzato")
    client.close()

if __name__ == "__main__":
    asyncio.run(init_database())