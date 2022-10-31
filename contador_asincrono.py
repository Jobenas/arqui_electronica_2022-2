import time
import asyncio

async def cuenta():
    print("Uno")
    await asyncio.sleep(1)
    print("Dos")


async def main():
    # await asyncio.gather(*(cuenta() for _ in range(3)))
    await asyncio.gather(cuenta(), cuenta(), cuenta())


if __name__ == "__main__":
    inicio = time.perf_counter()
    asyncio.run(main())
    fin = time.perf_counter()

    print(f"Tiempo total de ejecucion:{fin - inicio:0.2f} segundos")