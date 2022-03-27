import socket
import time
import logging

class SnakeSocket:
    HEADER = 64
    PORT = 5054
    SERVER = socket.gethostbyname(socket.gethostname())
    FORMAT = "utf-8"
    ADDR = (SERVER, PORT)

    def setup(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(SnakeSocket.ADDR)        

    def send_data(self, msg):
        self.check_setup()

        message = msg.encode(SnakeSocket.FORMAT)
        msg_len = (str(len(message))).encode(SnakeSocket.FORMAT)
        msg_len += b" "*(SnakeSocket.HEADER-len(msg_len))
 
        self.client.send(msg_len)
        self.client.sendall(bytes(message))

    def incomming_data(self):
        self.check_setup()
        while True:
            msg_len = self.client.recv(SnakeSocket.HEADER).decode(SnakeSocket.FORMAT)
            if msg_len == "":
                continue
            data = self.client.recv(int(msg_len)).decode(SnakeSocket.FORMAT)
            logging.debug(f"Received data \"{data}\"")
            yield data
            
    def check_setup(self):
        if self.client is None:
            raise Exception("Before using socket need to call `Socket.setup()`")

snake_socket = SnakeSocket()

# For testing purposes
if __name__ == "__main__":
    snake_socket.setup()
    snake_socket.send_data("data")

    for index, data in enumerate(snake_socket.incomming_data()):
        print(f"Received =\"{data}\" | {index}-th message")
        snake_socket.send_data("test")
        time.sleep(1)       
