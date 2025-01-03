import asyncio
import websockets
import json
async def listen():
    url = "ws://localhost:8765"
    message_type = input("Enter message type: ")
    message_text = input("Enter message : ")
    
    async with websockets.connect(url) as ws:
        final_message = {"type": message_type,"text": message_text}
        await ws.send(json.dumps(final_message))
        while True:
            server_msg = await ws.recv()
            print(f"Server says: {server_msg}")
            
asyncio.get_event_loop().run_until_complete(listen())
