import Scripts.Responses
import Scripts.AdminRequests
import Scripts.UserDetailsChecker
import Scripts.LogWriter
import json
import socket


def invalid_request(client_socket, msg):
    client_socket.sendall(json.dumps(Scripts.Responses.invalid_request()).encode())
    client_socket.close()
    Scripts.LogWriter.invalid_request(msg["Username"], msg["Request"], msg["Time"])


def wrong_password(client_socket, msg):
    client_socket.sendall(json.dumps(Scripts.Responses.wrong_password()).encode())
    client_socket.close()
    Scripts.LogWriter.wrong_password(msg["Username"], msg["Time"])


def compare_times(t1, t2):
    t1 = t1.split(" ")
    t2 = t2.split(" ")
    if t1[1] == "PM" and t2[1] == "AM":  # part in day
        return True
    elif t1[1] == "AM" and t2[1] == "PM":
        return False
    
    t1 = t1[0].split(":")
    t2 = t2[0].split(":")
    print(t1, t2)
    print(int(t1[0]), int(t1[1]), int(t1[2]), int(t2[0]), int(t2[1]), int(t2[2]))
    if int(t1[0]) > int(t2[0]):  # hours
        return True
    elif int(t1[0]) < int(t2[0]):
        return False
    elif int(t1[1]) > int(t2[1]):  # minutes
        return True
    elif int(t1[1]) < int(t2[1]):
        return False
    elif int(t1[2]) > int(t2[2]):  # seconds
        return True
    elif int(t1[2]) < int(t2[2]):
        return False
    return False  # equal


def fresh_game(client_socket, games, msg):
    last_update = msg["Content"]
    send = last_update == ""
    for game in games:
        if not send:
            send = compare_times(game[1], last_update)
        if send:
            if game[0] is not None:
                client_socket.sendall((json.dumps(Scripts.Responses.fresh_game(game[0]))).encode())
                client_socket.recv(1024)
    client_socket.sendall((json.dumps(Scripts.Responses.end())).encode())
    client_socket.recv(1024)
    client_socket.close()
    Scripts.LogWriter.game_fresh(msg["Username"], msg["Time"])


def fresh_pit(client_socket, pits, msg):
    client_socket.sendall(json.dumps(Scripts.Responses.fresh_pit(pits)).encode())
    client_socket.close()
    Scripts.LogWriter.pit_fresh(msg["Username"], msg["Time"])


def add_game(client_socket, msg):
    client_socket.sendall(json.dumps(Scripts.Responses.fine()).encode())
    client_socket.close()
    Scripts.LogWriter.game_addition(msg["Content"], msg["Username"], msg["Time"])
    return msg["Content"], msg["Time"]


def add_pit(client_socket, msg):
    client_socket.sendall(json.dumps(Scripts.Responses.fine()).encode())
    client_socket.close()
    Scripts.LogWriter.pit_addition(msg["Content"], msg["Username"], msg["Time"])
    return msg["Content"], msg["Time"]


def change_admin_password(client_socket: socket, user_info: dict, msg: dict) -> dict:
    user_info = Scripts.AdminRequests.change_self_password(msg["Content"], user_info)
    client_socket.sendall(json.dumps(Scripts.Responses.fine()).encode())
    client_socket.close()
    Scripts.LogWriter.admin_password_changed(msg["Time"])
    return user_info


def change_user_password(client_socket, msg, user_info):
    user = msg["Content"]
    if not Scripts.UserDetailsChecker.check_existing_username(user, user_info):
        client_socket.sendall(json.dumps(Scripts.Responses.user_not_found(user)).encode())
        return
    client_socket.sendall(json.dumps(Scripts.Responses.fine()).encode())
    new_password = client_socket.recv(1024).decode()
    new_password = json.loads(new_password)
    user_info = Scripts.AdminRequests.change_user_password(new_password["Content"], user, user_info)
    client_socket.sendall(json.dumps(Scripts.Responses.fine()).encode())
    client_socket.close()
    Scripts.LogWriter.user_password_changed(msg["Content"], msg["Time"])
    return user_info


def block_user(client_socket, msg, user_info):
    # TODO: implement block_user
    if not Scripts.UserDetailsChecker.check_existing_username(msg["Content"], user_info):
        client_socket.sendall(json.dumps(Scripts.Responses.user_not_found(msg["Content"])).encode())
        client_socket.close()
        return
    Scripts.AdminRequests.block_user(msg["Content"], user_info)
    client_socket.sendall(json.dumps(Scripts.Responses.fine()).encode())
    client_socket.close()
    Scripts.LogWriter.user_blocked(msg["Content"], msg["Time"])


def unblock_user(client_socket, msg, user_info):
    # TODO: implement unblock_user
    raise NotImplementedError
    pass


def create_user(client_socket: socket.socket, msg, user_info: dict):
    if msg["Content"] in user_info.keys():
        client_socket.sendall(json.dumps(Scripts.Responses.user_already_exists(msg["Content"])).encode())
        return user_info
    user_info[msg["Content"]] = ""
    client_socket.sendall(json.dumps(Scripts.Responses.fine()).encode())
    password = json.loads(client_socket.recv(1024).decode())
    user_info[msg["Content"]] = password["Content"]
    client_socket.close()
    return user_info