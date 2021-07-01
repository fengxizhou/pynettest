import argparse
import socketserver
from typing import Any


class MyTCPHandler(socketserver.BaseRequestHandler):
    def __init__(self, request: Any, client_address: Any, server: socketserver.BaseServer):
        super().__init__(request, client_address, server)
        self.data = ""

    def handle(self):
        self.data = self.request.recv(1024).strip()
        print("{} wrote: {}".format(self.client_address[0], self.data))
        self.echo()

    def echo(self):
        self.request.sendall(self.data.upper())


def server(host, port):
    with socketserver.TCPServer((host, port), MyTCPHandler) as svr:
        svr.serve_forever()


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument("host")
    p.add_argument("port", type=int)
    args = p.parse_args()

    server(args.host, args.port)
