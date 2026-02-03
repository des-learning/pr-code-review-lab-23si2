import json
import os
from typing import Dict, Any, List

def load_users(file_path: str = "data/users.json") -> List[Dict[str, Any]]:
    """Safely load users from JSON. Returns empty list if missing/corrupt."""
    if not os.path.exists(file_path):
        print(f"Info: {file_path} not found. Starting with empty users.")
        return []
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            print("Warning: Invalid users format. Starting empty.")
            return []
    except (json.JSONDecodeError, IOError) as e:
        print(f"Error loading users: {e}. Using empty list.")
        return []

def save_users(users: List[Dict[str, Any]], file_path: str = "data/users.json") -> bool:
    """Atomically save users to JSON."""
    os.makedirs(os.path.dirname(file_path) or '.', exist_ok=True)
    temp_path = file_path + '.tmp'
    try:
        with open(temp_path, 'w') as f:
            json.dump(users, f, indent=2)
        os.replace(temp_path, file_path)  
        return True
    except IOError as e:
        print(f"Failed to save users: {e}")
        if os.path.exists(temp_path):
            os.remove(temp_path)
        return False
