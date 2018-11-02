import datetime


BASE = {
    "Message": "",
    "Content": "",
    "Time": ""
}


def fine():
    resp = dict(BASE)
    resp["Message"] = "Fine"
    resp["Time"] = str(datetime.datetime.now())
    return resp


def wrong_password():
    resp = dict(BASE)
    resp["Message"] = "Wrong password"
    resp["Time"] = str(datetime.datetime.now())
    return resp


def user_already_exists(user):
    resp = dict(BASE)
    resp["Message"] = "User already exists"
    resp["Content"] = user
    resp["Time"] = str(datetime.datetime.now())
    return resp


def user_not_found(user):
    resp = dict(BASE)
    resp["Message"] = "User not found"
    resp["Content"] = user
    resp["Time"] = str(datetime.datetime.now())
    return resp


def user_already_blocked(user):
    resp = dict(BASE)
    resp["Message"] = "User already blocked"
    resp["Content"] = user
    resp["Time"] = str(datetime.datetime.now())
    return resp


def block_admin():
    resp = dict(BASE)
    resp["Message"] = "You can not block the admin!"
    resp["Content"] = "I'm the best server in town BABY!"
    resp["Time"] = str(datetime.datetime.now())
    return resp


def user_blocked():
    resp = dict(BASE)
    resp["Message"] = "BLOCKED"
    resp["Content"] = "This user is blocked, sorry"
    resp["Time"] = str(datetime.datetime.now())
    return resp


def invalid_request():
    resp = dict(BASE)
    resp["Message"] = "Invalid Request!"
    resp["Time"] = str(datetime.datetime.now())
    return resp


def fresh_game(games):
    resp = dict(BASE)
    resp["Message"] = "fine"
    resp["Content"] = games
    resp["Time"] = str(datetime.datetime.now())
    return resp


def end():
    resp = dict(BASE)
    resp["Message"] = "End"
    resp["Content"] = ""
    resp["Time"] = str(datetime.datetime.now())
    return resp


def fresh_pit(pits):
    resp = dict(BASE)
    resp["Message"] = "fine"
    resp["Content"] = pits
    resp["Time"] = str(datetime.datetime.now())
    return resp
