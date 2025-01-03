import asyncio
import websockets
import json
PORT = 8765

connected = set()

async def echo(websocket,path):
    print("client connected")
    connected.add(websocket)
    try:
        async for message in websocket:
            message = json.loads(message)
            # print(type(message))
            # print(message["type"])
            if message["type"] == "request":
                await websocket.send("Thinking on your request...")
                for conn in connected:
                    if conn != websocket:
                        await conn.send("another client is requesting - "+message["text"])
            print(f"Received message: {message}")
    except websockets.exceptions.ConnectionClosed as e:
        print(f"Connection closed")
        pass
        
server = websockets.serve(echo, "localhost", PORT)
asyncio.get_event_loop().run_until_complete(server)
asyncio.get_event_loop().run_forever()