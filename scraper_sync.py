import requests
import time

def get_site(url: str, session: requests.Session):
    with session.get(url) as response:
        print(f"Lei {len(response.content)} bytes de {url}")


def get_all(sites: list[str]):
    with requests.Session() as session:
        for url in sites:
            get_site(url, session)
        

if __name__ == "__main__":
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80

    inicio = time.perf_counter()
    get_all(sites)
    fin = time.perf_counter()

    print(f"Descarga sincrona completa en {fin - inicio} segundos")