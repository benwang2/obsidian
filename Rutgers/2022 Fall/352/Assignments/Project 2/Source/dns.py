from symbol import pass_stmt
import threading
import time
import socket

class Record():
    def __init__(self, name, type, value):
        self.name = name
        self.type = type
        self.value = value

class DNS():
    def __init__(self, hostname, records):
        self.hostname = hostname.lower()
        self.map = {}
        self.socket = None

        for record in records:
            self.map[record.name.lower()] = record.value

    def listen(self):
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print("[S]: Server socket created")
        except socket.error as err:
            print('socket open error: {}\n'.format(err))
            exit()

        server_binding = ('', 53)
        self.socket.bind(server_binding)
        self.socket.listen(1)

        dns_hostname = socket.gethostname()
        print("[S]: DNS host name is {}".format(dns_hostname))
        print("[S]: Server IP address is {}".format(socket.gethostbyname(dns_hostname)))

        lsid, addr = self.socket.accept()

        while True:
            received = self.socket.recv(4096)

            hostname = received.strip().lower()

            if hostname in self.map:
                record = self.map[hostname]
                response = " ".join(hostname, record.name, "A", "IN")
                self.socket.send()
            else:
                pass

            if not received:
                break

            data = received.decode('utf-8')