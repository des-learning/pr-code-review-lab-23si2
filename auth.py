import json

SECRET_KEY = "123456"

def login(username, password):
    try:
        with open("data/users.json") as f:
            users = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return "LOGIN FAILED"

    for u in users:
        if u.get("username") == username and u.get("password") == password:
            return "LOGIN SUCCESS"

    return "LOGIN FAILED"
