import json
import socket
import Scripts.Serialization
import Scripts.HandleRequests
import Scripts.UserDetailsChecker
import Scripts.LogWriter

LISTEN_PORT = 3388
GAMES = Scripts.Serialization.load_games()
PITS = Scripts.Serialization.load_pits()


def main():
    user_details = Scripts.Serialization.load_user_info()
    listen_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ("", LISTEN_PORT)

    try:
        listen_sock.bind(server_address)
    except OSError:
        print("The port is already used.. :(")
        return

    listen_sock.listen(1)
    for i in range(0, 20):
        try:
            client_sock, client_address = listen_sock.accept()
            client_msg = client_sock.recv(1024).decode()
            client_msg = json.loads(client_msg)
            Scripts.LogWriter.new_connection(client_address, client_msg["Username"], client_msg["Time"])
        except ConnectionResetError:
            continue
        if not get_access(client_msg, user_details):
            Scripts.HandleRequests.wrong_password(client_sock, client_msg)
            continue
        if client_msg["Username"] == "Admin" and client_msg["Request"] not in ["Load", "Upload"]:
            user_details = HandleRequestAdmin(client_sock, user_details, client_msg)
        HandleRequest(client_msg, client_sock)

    listen_sock.close()
    return user_details


def get_access(msg, user_details):
    return Scripts.UserDetailsChecker.check_password(msg["Username"], msg["Password"], user_details)


def HandleRequestAdmin(client_sock, user_info, msg):
    # TODO: implement the Admin Request Handling
    if msg["Request"] == "ChangePassSelf":
        user_info = Scripts.HandleRequests.change_admin_password(client_sock, user_info, msg)
    elif msg["Request"] == "ChangePassUser":
        user_info = Scripts.HandleRequests.change_user_password(client_sock, msg, user_info)
    elif msg["Request"] == "ShowLog":
        client_sock.sendall(Scripts.Serialization.read_all(Scripts.Serialization.DATA_LOG_PATH).encode())
    Scripts.Serialization.save_user_info(user_info)
    return user_info


def HandleRequest(msg, client_socket):
    request = msg["Request"] + msg["Type"]

    if request == "UploadPit":
        PITS.append(Scripts.HandleRequests.add_pit(client_socket, msg))
        print(PITS)
    elif request == "UploadGame":
        GAMES.append(Scripts.HandleRequests.add_game(client_socket, msg))
        print(GAMES)
    elif request == "LoadGame":
        Scripts.HandleRequests.fresh_game(client_socket, GAMES, msg)
    elif request == "LoadPit":
        Scripts.HandleRequests.fresh_pit(client_socket, PITS, msg)
    else:
        Scripts.HandleRequests.invalid_request(client_socket, msg)


if __name__ == '__main__':
    while True:
        Scripts.Serialization.save_user_info(main())
        Scripts.Serialization.save_pits(PITS)
        Scripts.Serialization.save_games(GAMES)
