import json
import hashlib
import os

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(username, password):
    users_file = "data/users.json"

    # Pastikan folder & file ada
    if not os.path.exists("data"):
        os.mkdir("data")

    if os.path.exists(users_file):
        try:
            with open(users_file) as f:
                users = json.load(f)
        except json.JSONDecodeError:
            raise Exception("User data corrupted")
    else:
        users = []

    # Cek username duplicate
    for user in users:
        if user.get("username") == username:
            raise Exception("Username already exists")

    users.append({
        "username": username,
        "password": hash_password(password)
    })

    with open(users_file, "w") as f:
        json.dump(users, f, indent=2)
