import socket


HEADER = 64
PORT = 5050
SERVER = "127.0.1.1"
FORMAT = "utf-8"
ADDR = (SERVER, PORT)


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_len = (str(len(message))).encode(FORMAT)
    msg_len += b" "*(HEADER-len(msg_len))
    client.send(msg_len)
    client.send(message)


send("hey")
input()
send("/Disconnect")
    
