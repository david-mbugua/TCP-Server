import socket


class TCPServer:
    def __init__(self, max_clients=5):
        self.max_clients = max_clients
        self.clients = {}

    def start(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('0.0.0.0', 1234))
        sock.listen(self.max_clients)
        print(f'Listening for {self.max_clients} clients...')

        while True:
            client, address = sock.accept()
            rank = len(self.clients)
            self.clients[rank] = client
            print(f'Client {rank} connected from {address}')
            client.send(f'Welcome, you have been assigned rank {rank}'.encode())

            while True:
                data = client.recv(1024).decode()
                if not data:
                    break
                self.handle_command(rank, data)

            del self.clients[rank]
            self.promote_clients(rank)

    def handle_command(self, sender_rank, data):
        for rank, client in self.clients.items():
            if rank > sender_rank:
                client.send(data.encode())

    def promote_clients(self, disconnected_rank):
        for rank in range(disconnected_rank, len(self.clients)):
            self.clients[rank] = self.clients[rank + 1]
        del self.clients[len(self.clients)]


if __name__ == '__main__':
    server = TCPServer()
    server.start()
