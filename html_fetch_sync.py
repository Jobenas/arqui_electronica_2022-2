import requests
import time

def fetch_url(url: str) -> int:
    print(f"Iniciando operacion en url {url}")
    resp = requests.get(url)

    return resp.status_code

def main():
    with open("urls.txt", "r") as f:
        contenido = f.read()
    
    urls = contenido.split("\n")

    for url in urls:
        status = fetch_url(url)
        print(f"URL: {url} - Status: {status}")

if __name__ == "__main__":
    inicio = time.perf_counter()
    main()
    fin = time.perf_counter()

    print(f"Tiempo total de ejecucion:{fin - inicio:0.2f} segundos")