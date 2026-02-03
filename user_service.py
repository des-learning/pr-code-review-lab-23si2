import json
from pathlib import Path
import bcrypt
from threading import Lock  
DATA_FILE = Path("data/users.json")
lock = Lock()

def init_users_file():
    if not DATA_FILE.exists():
        DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
        DATA_FILE.write_text("[]")

def register_user(username: str, password: str) -> str:
    if not username or not password:
        return "Username and password must be filled"

    init_users_file()

    with lock:   
        try:
            data = DATA_FILE.read_text()
            users = json.loads(data) if data.strip() else []
        except:
            users = []

        # Check password duplicate
        if any(u["username"] == username for u in users):
            return "Username is being used"

        # Hash password
        hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt(rounds=12))

        users.append({
            "username": username,
            "password": hashed.decode()   
        })

        DATA_FILE.write_text(json.dumps(users, indent=2))

    return "User created successfully"