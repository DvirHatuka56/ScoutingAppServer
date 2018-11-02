import json
import codecs

USER_INFO_PATH = "Files\\UsersInfo.json"
GAMES_PATH = "Files\\GamesBackup.json"
PITS_PATH = "Files\\PitsBackup.json"
ADMIN_LOG_PATH = "Files\\AdminLog.txt"
DATA_LOG_PATH = "Files\\DataLog.txt"


def write_in_file(file_name, message, write_type="w"):
    with codecs.open(file_name, write_type, "utf-8") as writer:
        writer.write(message)


def read_all(file_name):
    with codecs.open(file_name, "r", "utf-8") as reader:
        return reader.read()


def save_user_info(user_info):
    write_in_file(USER_INFO_PATH, json.dumps(user_info))


def load_user_info():
    return json.loads(read_all(USER_INFO_PATH))


def save_games(games):
    write_in_file(GAMES_PATH, json.dumps(games))


def load_games():
    return json.loads(read_all(GAMES_PATH))


def save_pits(games):
    write_in_file(PITS_PATH, json.dumps(games))


def load_pits():
    return json.loads(read_all(PITS_PATH))


def write_in_admin_log(activity):
    write_in_file(ADMIN_LOG_PATH, activity, write_type="a")


def write_in_data_log(activity):
    write_in_file(DATA_LOG_PATH, activity, write_type="a")


def clear_admin_log():
    write_in_file(ADMIN_LOG_PATH, "")


def clear_data_log():
    write_in_file(DATA_LOG_PATH, "")
