import json

DATA_PATH = "data/users.json"

def login(username, password):
    try:
        with open(DATA_PATH) as f:
            users = json.load(f)
    except FileNotFoundError:
        return "User data not found"

    for user in users:
        if user["username"] == username and user["password"] == password:
            return "LOGIN SUCCESS"

    return "LOGIN FAILED"
