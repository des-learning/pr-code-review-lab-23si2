import json

def register_user(username, password):
    if not username or not password:
        return

    with open("data/users.json") as f:
        users = json.load(f)

    users.append({
        "username": username,
        "password": password
    })

    with open("data/users.json", "w") as f:
        json.dump(users, f)
