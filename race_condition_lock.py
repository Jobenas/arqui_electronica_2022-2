import time
import concurrent.futures
from threading import Lock

class FakeDatabase:
    def __init__(self):
        self.value = 0
        self.lock = Lock()

    def update(self, name):
        print(f"Thread {name}: iniciando actualización")
        print(f"Thread {name}: a punto de obtener el candado")

        with self.lock:
            print(f"Thread {name}: obtuvo el candado")
            local_copy = self.value
            local_copy +=1
            time.sleep(0.1)
            self.value = local_copy
            print(f"Thread {name}: liberando el candado")

        print(f"Thread {name}: ha liberado el candado")
        print(f"Thread {name}: terminando actualización")

if __name__ == "__main__":
    workers = 10
    db = FakeDatabase()
    print(f"Valor inicial de la base de datos: {db.value}")

    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
        for index in range(workers):
            executor.submit(db.update, index)
    
    print(f"Valor final de la base de datos: {db.value}")
