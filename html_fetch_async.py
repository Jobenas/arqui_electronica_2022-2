import asyncio 
import time

from aiohttp import ClientSession

async def fetch_url(url: str, session: ClientSession, **kwargs) -> int:
    print(f"Iniciando operacion en url {url}")
    try:
        resp = await session.request(method='GET', url=url, **kwargs)
        resp.raise_for_status()

        print(f"URL: {url} - Status: {resp.status}")
        return resp.status
    except Exception as e:
        print(f"URL: {url} - Status: 404")
        return 404


async def main():
    with open("urls.txt", "r") as f:
        contenido = f.read()
    
    urls = contenido.split("\n")

    async with ClientSession() as session:
        tasks = []
        for url in urls:
            tasks.append(fetch_url(url, session))
        await asyncio.gather(*tasks)


if __name__ == "__main__":
    inicio = time.perf_counter()
    asyncio.run(main())
    fin = time.perf_counter()

    print(f"Tiempo total de ejecucion:{fin - inicio:0.2f} segundos")
