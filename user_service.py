import json
import sys

def register_user(username, password):
    with open("data/users.json") as f:
        try:
            users = json.load(f)
        except json.JSONDecodeError:
            users = []


    users.append({
        "username": username,
        "password": password
    })

    with open("data/users.json", "w") as f:
        json.dump(users, f)

