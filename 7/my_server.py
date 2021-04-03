import socket
from threading import Thread

HOST = '127.0.0.1'
TCP_PORT = 5555
UDP_PORT = 7777


def tcp_server():
    print("I'm tcp_server!")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((HOST, TCP_PORT))
        sock.listen()
        print(f"Waiting for TCP connections...")
        while True:
            conn, addr = sock.accept()
            with conn:
                data = conn.recv(1024)
                print(f"TCP server: Received data: {data.decode()} from {addr}")
                if not data:
                    break
                conn.send(f"tcp_server: You sent '{data.decode()}'".encode())


def udp_server():
    print("I'm udp_server!")
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.bind((HOST, UDP_PORT))
        print(f"Waiting for UDP connections...")
        while True:
            data, addr = sock.recvfrom(1024)
            if not data:
                break
            print(f"UDP server: Received data {data.decode()} from {addr}")
            sock.sendto(f"udp_server: You sent '{data.decode()}'".encode(), addr)


if __name__ == '__main__':
    print("Hello")
    t1 = Thread(target=tcp_server)
    t2 = Thread(target=udp_server)
    threads = [t1, t2]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
