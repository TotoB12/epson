import epson_projector as epson
from epson_projector.const import (PWR_OFF)

import asyncio
import aiohttp

# L-102  172.16.16.162
# L-104 172.16.16.119
# L-105  172.16.16.173
# L-201  172.16.16.153
# L-205  172.16.16.168
# L-107 172.16.68.184
# L-203 172.16.68.91
# L-206  172.16.16.171
# C-10  172.16.16.154
# C-12  172.16.16.167
# C-22 172.16.16.160
# C-24  172.16.16.149
# C-25 172.16.16.164
# C-27  172.16.16.169
# C-ART  172.16.16.155
projectors = [172.16.16.162, 172.16.16.119, 172.16.16.173, 172.16.16.153, 172.16.16.168, 172.16.16.171, 172.16.16.154, 172.16.16.167, 172.16.16.160, 172.16.16.149, 172.16.16.169, 172.16.16.155, 172.16.68.184, 172.16.68.91]

async def main():
    async with aiohttp.ClientSession() as session:
        for projector in projectors:
            try:
                await run(session, projector)
                print(f'Turned Off {projector}')
            except Exception as e:
                print(f'Could not turn off {projector}: {e}')

async def run(websession, projector):    
    projector = epson.Projector(
        host=projector,
        websession=websession)
    data = await projector.send_command(PWR_OFF)
    print(data)

asyncio.get_event_loop().run_until_complete(main()) 
