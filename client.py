import socket
import threading

HOST = "127.0.0.1"
PORT = 5555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

print("Connected to the server!")


def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode()
            print("\n" + message)
        except:
            print("Disconnected from server")
            client.close()
            break


thread = threading.Thread(target=receive_messages)
thread.start()


while True:
    message = input("You: ")
    client.send(message.encode())