LAN Chat Application

A real-time text chat application built using Python socket programming.
The application follows a client-server architecture and allows multiple users to communicate with each other over a local network (LAN).

Features

- Real-time messaging between multiple users.
- Client-server architecture using TCP sockets.
- Supports multiple connected clients.
- Messages are routed from the server to all connected users.
- Works on a local network (Wi-Fi/LAN).

Technologies Used

- Python 3
- Socket Programming
- TCP/IP Networking
- Threading for handling multiple clients

Project Structure

lan-chat.app/
│
├── server.py      # Server-side application
├── client.py      # Client-side application
└── README.md      # Project documentation

How It Works

The application uses a server-client model:

1. The server starts and listens for incoming client connections.
2. Clients connect to the server using the server IP address and port number.
3. Each client can send messages to the server.
4. The server receives messages and broadcasts them to all connected clients.

Network Setup (LAN)

To run the application on the same local network:

On the Server Computer

1. Open the terminal.
2. Run:

python server.py

3. Find the server computer's local IP address:

Windows:

ipconfig

Look for the IPv4 Address.

On Client Computers

1. Open the terminal.
2. Run:

python client.py

3. Enter the server IP address and port number.
4. Start chatting.

Socket Communication

The project uses TCP sockets to create reliable communication between clients and the server.

- The server uses a socket to listen for connections.
- Each client creates a socket to connect to the server.
- The server maintains a list of connected clients.
- When a message is received, the server forwards it to the connected users.

Installation

Make sure Python is installed:

python --version

No external libraries are required.

Future Improvements

- Add user authentication.
- Add private messaging.
- Create a graphical user interface.
- Store chat history.

Author

Salma 