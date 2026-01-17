import asyncio
import json
import random
from tornado.websocket import websocket_connect

# Indirizzo del tuo server Tornado
WS_URL = "ws://127.0.0.1:8888/points"


async def match_simulator(match_id):
    print(f"[MATCH {match_id}] Avviato")
    try:
        ws = await websocket_connect(WS_URL)
        while True:

            team = random.choice(["A", "B"])
            payload = {"match_id": match_id, "team": team}
            ws.write_message(json.dumps(payload))
            await asyncio.sleep(random.uniform(0.5, 1.0))

    except Exception as e:
        print(f"❌ Errore match {match_id}: {e}")


async def main():
    print("Publisher Beach Volley avviato")
    tasks = []
    for i in range(1, 9):
        tasks.append(match_simulator(i))
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nSimulazione interrotta.")