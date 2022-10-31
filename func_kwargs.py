def func(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")


if __name__ == "__main__":
    func(nombre="Juan", apellido="Perez", edad=30)
    func(username="jperez", password="123456")