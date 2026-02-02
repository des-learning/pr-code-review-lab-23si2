import json

def login(username, password):
    # Validasi input
    if not username or not password:
        raise ValueError("Username dan password wajib diisi")

    try:
        with open("data/users.json", "r") as f:
            users = json.load(f)
    except FileNotFoundError:
        raise RuntimeError("File data user tidak ditemukan")
    except json.JSONDecodeError:
        raise RuntimeError("Format data user tidak valid")

    # Proses autentikasi TANPA ubah struktur JSON
    for user in users:
        if (
            user.get("username") == username
            and user.get("password") == password
        ):
            return "LOGIN SUCCESS"

    return "LOGIN FAILED"
