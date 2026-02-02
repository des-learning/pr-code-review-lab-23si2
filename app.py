from auth import login
from user_service import register_user

def main():
    print("Welcome to User System")

    action = input("login/register: ").strip().lower()

    if action == "login":
        username = input("username: ").strip()
        password = input("password: ").strip()

        if not username or not password:
            print("Username dan password tidak boleh kosong")
            return

        try:
            result = login(username, password)
            print(result)
        except Exception as e:
            print(f"Login gagal: {e}")

    elif action == "register":
        username = input("username: ").strip()
        password = input("password: ").strip()

        if not username or not password:
            print("Username dan password tidak boleh kosong")
            return

        try:
            register_user(username, password)
            print("User berhasil dibuat")
        except Exception as e:
            print(f"Registrasi gagal: {e}")

    else:
        print("Unknown action. Silakan pilih 'login' atau 'register'.")

if __name__ == "__main__":
    main()
