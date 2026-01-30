import json
import os

def register_user(username, password):
    # Validate input
    if not username or not password:
        return "Username and password cannot be empty"

    # Ensure the users data file exists
    if not os.path.exists("data/users.json"):
        return "User data file not found"
    
    # Load existing users
    try:
        with open("data/users.json") as f:
            users = json.load(f)
    except json.JSONDecodeError:
        return "Error decoding user data"

    # Append new user
    users.append({
        "username": username,
        "password": password
    })

    # Write updated user data to file
    try:
        with open("data/users.json", "w") as f:
            json.dump(users, f)
    except IOError:
        return "Error saving user data"

    return "User registered successfully"
