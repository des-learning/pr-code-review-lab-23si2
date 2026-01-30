import json

SECRET_KEY = "123456"  # hardcoded secret 😬

def login(username, password):
    # Validate input
    if not username or not password:
        return "Username and password cannot be empty"

    # Load users data from file
    try:
        with open("data/users.json") as f:
            users = json.load(f)
    except FileNotFoundError:
        return "User data file not found"
    except json.JSONDecodeError:
        return "Error decoding user data"

    # Check if user exists and password match
    for user in users:
        if user["username"] == username and user["password"] == password:
            return "LOGIN SUCCESS"

    return "LOGIN FAILED"
