import json
import hashlib


def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()


def register_user(username, password):
    try:
        with open("data/users.json") as f:
            users = json.load(f)
    except FileNotFoundError:
        users = []

    # cek username duplikat
    for u in users:
        if u["username"] == username:
            return None

    users.append({
        "username": username,
        "password": hash_password(password)
    })

    with open("data/users.json", "w") as f:
        json.dump(users, f, indent=2)

    return {
        "username": username
    }