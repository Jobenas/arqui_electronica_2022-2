import socket
import time
import random


SOCK_BUFFER = 4

if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 5001)
    print(f"Conectando al servidor en {server_address[0]} y puerto {server_address[1]}")

    sock.connect(server_address )
    try:
        for i in range(10):
            msg = f"Este es el mensaje. Será enviado en trozos de {SOCK_BUFFER} bytes"
            msg = msg.encode('utf-8')
            print(f"logitud del mensaje: {len(msg)} bytes")
            sock.sendall(msg)
            amnt_recvd = 0
            amnt_expected = len(msg)
            msg_total_bytes = b''

            while amnt_recvd < amnt_expected:
                data = sock.recv(SOCK_BUFFER)
                print(f"Recibido: {data}")
                msg_total_bytes += data
                amnt_recvd += len(data)

            print(f"Recibido {msg_total_bytes.decode('utf-8')}")

            time.sleep(random.randint(1, 4))
    finally:
        print("Cerrando socket")
        sock.close()