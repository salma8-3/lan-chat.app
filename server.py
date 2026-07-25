import socket
import threading

HOST = "0.0.0.0"
PORT = 5555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print(f"Server is running on port {PORT}")

clients = []


def broadcast(message, sender):
    for client in clients:
        if client != sender:
            client.send(message)


def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            print(message.decode())
            broadcast(message, client)

        except:
            clients.remove(client)
            client.close()
            break


while True:
    client, address = server.accept()
    print(f"New connection from {address}")

    clients.append(client)

    thread = threading.Thread(
        target=handle_client,
        args=(client,)
    )
    thread.start()
