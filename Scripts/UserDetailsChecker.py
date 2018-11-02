def check_existing_username(username, user_details):
    return username in user_details.keys()


def check_password(username, password, user_details):
    if check_existing_username(username, user_details):
        return user_details[username] == password
    return False


def check_blocked_user(username, user_details):
    return "BLOCKED" in user_details[username]
