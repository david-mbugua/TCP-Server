# TCP Server

A simple TCP server that can accept and hold a maximum of N clients (where N is configurable). These clients are assigned ranks based on first-come-first-serve, i.e whoever connects first receives the next available high rank. Ranks are from 0–N, 0 being the highest rank. Clients can send to the server commands that the server distributes among the clients. Only a client with a lower rank can execute a command of a higher rank client. Higher rank clients cannot execute commands by lower rank clients, so these commands are rejected. The command execution can be as simple as the client printing to console that command has been executed. If a client disconnects the server should re-adjust the ranks and promote any client that needs to be promoted not to leave any gaps in the ranks.

## Prerequisites

- Python 3.x

## Installation

1. Clone or download this repository

2. Run the server by running the command ```python server.py```

## Usage

- To start the server, run the command ```python server.py```
- To connect to the server, use a client application such as 'telnet' or 'nc' like this: ```telnet localhost 1234```
- After connecting, you should see a message that says "Welcome, you have been assigned rank [rank]", where [rank] 
is the rank that the server has assigned to you.
- You can then try sending commands from the connected client, and the commands should be executed by clients with lower ranks.

## Configuration

You can configure the maximum number of clients that the server can hold by passing an argument to the 'TCPServer' constructor,
e.g. 'server = TCPServer(10)' to allow a maximum of 10 clients.

## Expected Behavior

- When the server is started, it will start listening for incoming connections on IP address 0.0.0.0 and port 1234.
- When a client connects, the server will assign them a rank based on the number of clients that have already connected, 
and sends the client a message with their
