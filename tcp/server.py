from typing import Dict
import socket
from collections import deque
import threading
import time

from .env import ALLOWED_IP, PORT

# 입력받는 쓰레드와
def receive(sock: socket.socket, msgQueue: deque):
    while True:

        data = sock.recv(1024).decode("utf-8")  # blocking

        if data == "":
            print(f"{sock.getpeername()} connection is terminated")
            sock.close()

        msgQueue.append((sock, data))  # [0]: socket, [1]: data


# 출력 쓰레드 구분해서 작성
# 발송한 소켓을 제외한 모든 사용자에게 발송
def send(connectedUsers: dict, msgQueue: deque):
    print("send Thread Start")
    while True:
        time.sleep(0.01)
        if msgQueue:
            socketSend: socket.socket
            data: bytes

            socketSend, data = msgQueue.popleft()

            for sock in connectedUsers.values():

                sock: socket.socket
                # 발송한 소켓은 되받지 않음
                if socketSend == sock:
                    continue

                msg = f"{socketSend.getpeername()}>>{data}"

                try:
                    sock.send(msg.encode("utf-8"))
                except socket.error:  # catch type
                    print("connection is terminated")


if __name__ == "__main__":
    msgQueue = deque()
    connectedUsers = {}
    count = 0
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.bind((ALLOWED_IP, PORT))

    # allowed IP
    print(f"server is listening at {serverSocket.getsockname()}")
    serverSocket.listen()

    while True:
        # 3-way handshake
        connectionSocket, addr = serverSocket.accept()
        connectedUsers[count] = connectionSocket
        count += 1

        receiveThread = threading.Thread(
            target=receive,
            args=(
                connectionSocket,
                msgQueue,
            ),
        )
        receiveThread.start()

        sendThread = threading.Thread(
            target=send,
            args=(
                connectedUsers,
                msgQueue,
            ),
        )
        sendThread.start()
