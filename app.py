import asyncio
import websockets

# create handler for each connection
async def handler(websocket, path):
    data = await websocket.recv()
    reply = f"Data recieved as:  {data}!"
    print(reply + " send!")
    await websocket.send(reply)
 
async def main():
    async with websockets.serve(handler, "localhost", 3000):
        await asyncio.Future()  # run forever

asyncio.run(main())
