import json

DATA_PATH = "data/users.json"

def register_user(username, password):
    try:
        with open(DATA_PATH) as f:
            users = json.load(f)
    except FileNotFoundError:
        users = []

    for user in users:
        if user["username"] == username:
            return False  # user already exists

    users.append({
        "username": username,
        "password": password
    })

    with open(DATA_PATH, "w") as f:
        json.dump(users, f, indent=4)

    return True
