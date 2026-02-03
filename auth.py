import json
import hashlib
import os

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def login(username, password):
    if not os.path.exists("data/users.json"):
        return "USER DATA NOT FOUND"

    try:
        with open("data/users.json") as f:
            users = json.load(f)
    except json.JSONDecodeError:
        return "USER DATA CORRUPTED"

    hashed_input_password = hash_password(password)

    for user in users:
        if user.get("username") == username and user.get("password") == hashed_input_password:
            return "LOGIN SUCCESS"

    return "LOGIN FAILED"
