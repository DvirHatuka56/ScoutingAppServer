import Scripts.UserDetailsChecker


def change_self_password(new_password, user_info):
    user_info["Admin"] = new_password
    return user_info


def change_user_password(new_password, user, user_info):
    if not Scripts.UserDetailsChecker.check_existing_username(user, user_info):
        return
    user_info[user] = new_password
    return user_info


def block_user(user, user_info):
    if not Scripts.UserDetailsChecker.check_existing_username(user, user_info):
        return
    user_info[user] += "BLOCKED"
    return user_info


def unblock_user(user, user_info):
    if not Scripts.UserDetailsChecker.check_existing_username(user, user_info):
        return
    user_info[user] = user_info[user].replace("BLOCKED", "")
    return user_info


def add_user(user, password, user_info):
    if Scripts.UserDetailsChecker.check_existing_username(user, user_info):
        return user_info
    user_info[user] = password
    return user_info
