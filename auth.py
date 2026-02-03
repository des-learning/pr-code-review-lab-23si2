import json
import bcrypt


def load_users():
    with open("data/users.json", "r") as f:
        return json.load(f)


def validate_input(username, password):
    errors = []

    if not username or not password:
        errors.append("Username dan password tidak boleh kosong")

    if " " in username:
        errors.append("Username tidak boleh mengandung spasi")

    if len(username) < 3:
        errors.append("Username minimal 3 karakter")

    if len(password) < 6:
        errors.append("Password minimal 6 karakter")

    return errors


def login(username, password):
    
    username = username.strip()
    password = password.strip()

    errors = validate_input(username, password)
    if errors:
        return " | ".join(errors)

    users = load_users()

    for user in users:
        if user["username"] == username:
            if bcrypt.checkpw(
                password.encode("utf-8"),
                user["password"].encode("utf-8")
            ):
                return "LOGIN SUCCESS"

    return "LOGIN FAILED"
