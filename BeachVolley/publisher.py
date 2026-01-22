import asyncio
import json
import random
import os
from tornado.websocket import websocket_connect

SERVER_NAME = os.environ.get("SERVER_NAME", "web")  # 'web' è il nome del servizio nel yaml
WS_URL = f"ws://{SERVER_NAME}:8888/points"


async def match_simulator(match_id):
    print(f"[MATCH {match_id}] Connessione a {WS_URL}...")
    try:
        ws = await websocket_connect(WS_URL)
        print(f"[MATCH {match_id}] Connesso!")
        while True:
            team = random.choice(["A", "B"])
            payload = {"match_id": match_id, "team": team}
            ws.write_message(json.dumps(payload))
            # Aspetta tra 0.5 e 1 secondo prima del prossimo punto
            await asyncio.sleep(random.uniform(0.5, 1.0))

    except Exception as e:
        print(f"Errore match {match_id}: {e}")
        # Riprova la connessione dopo 5 secondi se fallisce
        await asyncio.sleep(5)
        await match_simulator(match_id)


async def main():
    print(f"Publisher Beach Volley avviato verso {WS_URL}")
    tasks = []
    # Simuliamo gli 8 match degli ottavi
    for i in range(1, 9):
        tasks.append(match_simulator(i))
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nSimulazione interrotta.")