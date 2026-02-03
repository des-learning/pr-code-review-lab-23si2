import json

SECRET_KEY = "123456"  # hardcoded secret 😬

def login(username, password):
    # Input validation
    if username is None or not isinstance(username, str) or username.strip() == "":
        return "Username tidak boleh kosong"

    if password is None or not isinstance(password, str) or password.strip() == "":
        return "Password tidak boleh kosong"

    with open("data/users.json") as f:
        users = json.load(f)

    for u in users:
        if u["username"] == username and u["password"] == password:
            return "LOGIN SUCCESS"

    return "LOGIN FAILED"
