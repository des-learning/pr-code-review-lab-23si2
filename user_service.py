import json

def register_user(username, password):
    if not username or not password:
        raise ValueError("Username dan password wajib diisi")

    try:
        with open("data/users.json", "r") as f:
            users = json.load(f)
    except FileNotFoundError:
        raise RuntimeError("File data user tidak ditemukan")
    except json.JSONDecodeError:
        raise RuntimeError("Format data user tidak valid")

    # Cek username sudah ada
    for user in users:
        if user.get("username") == username:
            raise ValueError("Username sudah terdaftar")

    # Tambah user TANPA ubah struktur JSON
    users.append({
        "username": username,
        "password": password
    })

    try:
        with open("data/users.json", "w") as f:
            json.dump(users, f)
    except IOError:
        raise RuntimeError("Gagal menyimpan data user")
