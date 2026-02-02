import json
import hashlib


def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()


def login(username, password):
    try:
        with open("data/users.json") as f:
            users = json.load(f)
    except FileNotFoundError:
        return "USER DATA NOT FOUND"

    hashed_input = hash_password(password)

    for u in users:
        if u["username"] == username and u["password"] == hashed_input:
            return "LOGIN SUCCESS"

    return "LOGIN FAILED"