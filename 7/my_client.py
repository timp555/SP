import socket
from threading import Thread

HOST = '127.0.0.1'
TCP_PORT = 5555
UDP_PORT = 7777


def tcp_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, TCP_PORT))
        sock.send('Hello, I am TCP client'.encode())
        data = sock.recv(1024)
        print(f'TCP client received message "{data.decode()}"')


def udp_client():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.connect((HOST, UDP_PORT))
        sock.sendto('Hello, I am UDP client'.encode(), (HOST, UDP_PORT))
        data = sock.recv(1024)
        print(f'UDP client received message "{data.decode()}"')


if __name__ == '__main__':
    t1 = Thread(target=tcp_client)
    t2 = Thread(target=udp_client)
    threads = [t1, t2]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
