import socket
import threading

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
FORMAT = "utf-8"
ADDR = (SERVER, PORT)
DISCONNECT_MSG = "/Disconnect"


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handleClient(conn, addr):
    print(f"Client connected at {addr}")
    while True:
        msg_len = conn.recv(HEADER).decode(FORMAT)
        if msg_len == "":
            continue
        msg = conn.recv(int(msg_len)).decode(FORMAT)
        if msg == DISCONNECT_MSG:
            break
        print(msg)
    conn.close()
    print(f"Client at {addr} has disconnected")



def start():
    server.listen()
    print(ADDR)
    while True:
        conn, addr = server.accept()
        threading.Thread(target=handleClient, args=(conn, addr)).start()
        print(f"Number of connected clients = {threading.active_count() - 1}")

print("Server starting")
start()


