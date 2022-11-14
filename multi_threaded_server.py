import socket
from threading import Thread

SOCK_BUFFER = 1024

t_counter = 0

def client_handler(conn, client_address):
    global t_counter

    t_counter += 1

    print(f"Cantidad de hilos en ejecucion actualmente: {t_counter}")

    try:
        print(f"Conexion establecida con {client_address}")
        while True:
            data = conn.recv(SOCK_BUFFER)
            if data:
                # data_conv = data.decode('utf-8')
                print(f"Recibi {data} de {client_address}")
                conn.sendall(data)
            else:
                break
    except ConnectionResetError:
        print("Conexion cerrada por el cliente abruptamente")
    finally:
        print("El cliente ha cerrado la conexion")
        conn.close()
    
    t_counter -= 1


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ("localhost", 5001)
    print(f"Conectando al servidor en {server_address[0]} y puerto {server_address[1]}")
    sock.bind(server_address)

    sock.listen(1)

    while True:
        print("Esperando conexiones")

        conn, client_address = sock.accept()

        t = Thread(target=client_handler, args=(conn, client_address))
        t.start()
