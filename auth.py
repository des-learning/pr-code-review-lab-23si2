import json
from pathlib import Path
import bcrypt  
DATA_FILE = Path("data/users.json")

def init_users_file():
    if not DATA_FILE.exists():
        DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
        DATA_FILE.write_text("[]")

def login(username: str, password: str) -> str:
    init_users_file()
    try:
        users = json.loads(DATA_FILE.read_text())
    except:
        return "System error"

    for user in users:
        if user["username"] == username:
            if bcrypt.checkpw(password.encode(), user["password"].encode()):
                return "you have login sucessfully"
            else:
                return "Sorry, but you have failed to login"
    return "Sorry, but we can't find user"