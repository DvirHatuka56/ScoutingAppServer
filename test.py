import socket
import json
import datetime

DST_IP = "localhost"
DST_PORT = 3388

REQUEST = {
    "Username": "Admin",
    "Password": "dvir",
    "Request": "AddUser",
    "Type": "Game",
    "Content": "Dvir56",
    "Time": ""
}

TEST = {
    "Username": "Admin",
    "Password": "dvir",
    "Request": "Load",
    "Type": "Game",
    "Content": "12345",
    "Time": ""
}


def main():
    for request in [REQUEST, TEST]:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = (DST_IP, DST_PORT)

        try:
            sock.connect(server_address)
        except ConnectionRefusedError:  # in case of the server isn't on
            print("Unable connect the server")
            return

        request["Time"] = str(datetime.datetime.now())
        sock.sendall(json.dumps(request).encode())
        print(sock.recv(1024).decode())
        if request["Request"] == "AddUser":
            request["Content"] = "Rewq2BZ8"
            request["Time"] = str(datetime.datetime.now())
            sock.sendall(json.dumps(request).encode())
            print(sock.recv(1024).decode())


if __name__ == '__main__':
    main()
