import epson_projector as epson
from epson_projector.const import (PWR_OFF)

import asyncio
import aiohttp
import ipaddress


async def main():
    async with aiohttp.ClientSession() as session:
        await run(session)


async def run(websession):
    # Use your local network subnet and starting IP for projectors
    network = ipaddress.ip_network('172.16.16.0/24')
    starting_ip = ipaddress.IPv4Address('172.16.16.100')
    tasks = []
    concurrency_limit = 25  # Set your preferred concurrency limit

    # Create a semaphore with a specified concurrency limit
    semaphore = asyncio.Semaphore(concurrency_limit)

    for ip in network:
        if ip >= starting_ip:
            tasks.append(turn_off_projector(websession, str(ip), semaphore))

    await asyncio.gather(*tasks)


async def turn_off_projector(websession, ip, semaphore):
    async with semaphore:
        try:
            projector = epson.Projector(
                host=ip,
                websession=websession
            )
            data = await projector.send_command(PWR_OFF)
            print(f"Projector at {ip} turned off: {data}")
        except Exception as e:
            print(f"Error turning off projector at {ip}: {e}")


asyncio.get_event_loop().run_until_complete(main())
