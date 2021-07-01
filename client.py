import argparse
import socket
import time


class MyClient:
    def __init__(self, host, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))

    def echo(self, data):
        self.sock.sendall(bytes(data + "\n", "utf-8"))
        send_time = time.time()
        received = str(self.sock.recv(1024), "utf-8")
        receive_time = time.time()

        print("Sent:     {}".format(data))
        print("Received: {}".format(received))
        print("Duration: {:.6f} seconds".format(receive_time - send_time))
        return data.upper() == received


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument("host")
    p.add_argument("port", type=int)
    p.add_argument("msg", nargs='+')
    args = p.parse_args()

    try:
        client = MyClient(args.host, args.port)
        local_ip = socket.gethostbyname_ex(socket.gethostname())[2][0]
        data = " ".join(args.msg)
        if client.echo(data):
            print("Network OK between {} and {}".format(args.host, local_ip))
        else:
            print("Network Error between {} and {}".format(args.host, local_ip))
    except Exception as e:
        print(e)
        print("Network between {} and {} test Failed!")
