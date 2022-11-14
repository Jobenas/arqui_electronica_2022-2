import time
import concurrent.futures


class FakeDatabase:
    def __init__(self):
        self.value = 0

    def update(self, name):
        print(f"Thread {name}: iniciando actualización")
        local_copy = self.value
        local_copy +=1
        self.value = local_copy
        time.sleep(0.1)
        print(f"Thread {name}: terminando actualización")


if __name__ == "__main__":
    workers = 2
    db = FakeDatabase()
    print(f"Valor inicial de la base de datos: {db.value}")
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
        for index in range(2):
            executor.submit(db.update, index)
    
    print(f"Valor final de la base de datos: {db.value}")

