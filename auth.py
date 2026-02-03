import json
from utils import load_users

SECRET_KEY = "123456"  # hardcoded secret 😬

def login(username, password):
    users = load_users()
    
    for user in users:  # readability
        if user["username"] == username and user["password"] == password:
            return "LOGIN SUCCESS"
    
    return "LOGIN FAILED"