import threading
import socket
from .env import HOST, PORT  # ip주소가 포함된 env.py 파일은 gitignore


def send(clientSocket: socket.socket):
    while True:
        message = input()  # blocking

        if message == "@exit":
            clientSocket.close()
            break

        try:
            clientSocket.send(message.encode("utf-8"))
        except socket.error:
            print("connection is terminated")
            break


def receive(clientSocket: socket.socket):
    while True:
        message = clientSocket.recv(1024).decode("utf-8")  # blocking

        if message == "@exit":
            clientSocket.close()
            break

        if not message:
            print(f"{clientSocket.getpeername()} is closed")
            clientSocket.close()
            break

        print(message)


clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((HOST, PORT))
MY_PORT = clientSocket.getsockname()
print("Connection to", HOST, PORT)
print(f"MY_PORT is {MY_PORT}")


sendingThread = threading.Thread(target=send, args=(clientSocket,))
receivingThread = threading.Thread(target=receive, args=(clientSocket,))
sendingThread.start()
receivingThread.start()

# 모든 쓰레드가 끝날 때 까지 대기
sendingThread.join()
receivingThread.join()

print(MY_PORT, "client is terminated")
