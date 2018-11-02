import Scripts.Serialization


def new_connection(address, user, time):
    Scripts.Serialization.write_in_data_log("Connection made: {0}:{1}, {2}|At: {3}\r".format(address[0], address[1],
                                                                                             user, time))
    print("Connection made: {0}:{1}, {2}|At: {3}\r".format(address[0], address[1], user, time))


def game_addition(game, user, time):
    Scripts.Serialization.write_in_data_log("Game added by {0} at {1} | Game: {2}\r".format(user, time, game))
    print("Game added by {0} at {1} | Game: {2}\r".format(user, time, game))


def pit_addition(pit, user, time):
    Scripts.Serialization.write_in_data_log("Pit added by {0} at {1} | Pit: {2}\r".format(user, time, pit))
    print("Pit added by {0} at {1} | Pit: {2}\r".format(user, time, pit))


def game_fresh(user, time):
    Scripts.Serialization.write_in_data_log("{0} requested to fresh games| At {1}\r".format(user, time))
    print("{0} requested to fresh games| At {1}\r".format(user, time))


def pit_fresh(user, time):
    Scripts.Serialization.write_in_data_log("{0} requested to fresh pits| At {1}\r".format(user, time))
    print("{0} requested to fresh pits| At {1}\r".format(user, time))


def wrong_password(user, time):
    Scripts.Serialization.write_in_data_log("{0} tried to access with wrong password| At {1}\r".format(user, time))
    print("{0} tried to access with wrong password| At {1}\r".format(user, time))


def admin_password_changed(time):
    Scripts.Serialization.write_in_admin_log("Admin password changed| At {0}\r".format(time))
    print("Admin password changed| At {0}\r".format(time))


def user_password_changed(user, time):
    Scripts.Serialization.write_in_admin_log("{0} password changed| At {1}\r".format(user, time))
    print("{0} password changed| At {1}\r".format(user, time))


def user_blocked(user, time):
    Scripts.Serialization.write_in_admin_log("{0} has been blocked| At {1}\r".format(user, time))
    print("{0} has been blocked| At {1}\r".format(user, time))


def user_unblocked(user, time):
    Scripts.Serialization.write_in_admin_log("{0} has been unblocked| At {1}\r".format(user, time))
    print("{0} has been unblocked| At {1}\r".format(user, time))


def user_addition(user, time):
    Scripts.Serialization.write_in_admin_log("{0} account has been created| At {1}\r".format(user, time))
    print("{0} account has been created| At {1}\r".format(user, time))


def invalid_request(user, request, time):
    Scripts.Serialization.write_in_admin_log("{0} send {1} request, unknown request|At {2}\r".format(user, request, time))
    print("{0} send {1} request, unknown request|At {2}\r".format(user, request, time))
