import epson_projector as epson
from epson_projector.const import (VOL_UP)
import time

import asyncio
import aiohttp


async def main():
    async with aiohttp.ClientSession() as session:
        await run(session)

host = input('Enter IP Address: ')

async def run(websession):    
    for i in range(0, 10):
        projector = epson.Projector(
            host=host,
            websession=websession)
        data = await projector.send_command(VOL_UP)
        print(data)
        time.sleep(0.5)

asyncio.get_event_loop().run_until_complete(main()) 

# 172.16.16.175