import json
import sys
from utils import load_users, save_users

def register_user(username, password):
    users = load_users()
    
    if any(u["username"] == username for u in users):
        print("Username already exists")
        return
    
    users.append({"username": username, "password": password})
    
    if save_users(users):
        print("User registered successfully")
    else:
        print("Failed to save new user")
        sys.exit(1)
