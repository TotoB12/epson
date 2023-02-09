import asyncio
import aiohttp
import epson_projector as epson
from epson_projector.const import PWR_OFF

async def main():
    async with aiohttp.ClientSession() as session:
        projects = await epson.discover(session)
        tasks = [turn_off(p, session) for p in projects]
        await asyncio.gather(*tasks)

async def turn_off(projector, session):
    p = epson.Projector(host=projector, websession=session)
    data = await p.send_command(PWR_OFF)
    print(f"Turned off {projector}: {data}")

asyncio.get_event_loop().run_until_complete(main())
