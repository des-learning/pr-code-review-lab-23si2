import json


def login(username, password):
    if not username or not password:
        return "LOGIN FAILED"

    try:
        with open("data/users.json", "r") as f:
            users = json.load(f)
    except FileNotFoundError:
        return "LOGIN FAILED"

    for user in users:
        if user["username"] == username and user["password"] == password:
            return "LOGIN SUCCESS"

    return "LOGIN FAILED"
