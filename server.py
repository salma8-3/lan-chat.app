import socket
import threading

HOST = "0.0.0.0"
PORT = 5555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print(f"Server is running on port {PORT}")

def handle_client(client):
    while True:
        message = client.recv(1024).decode()
        print(message)


while True:
    client, address = server.accept()
    print(f"New connection from {address}")

    thread = threading.Thread(target=handle_client, args=(client,))
    thread.start()