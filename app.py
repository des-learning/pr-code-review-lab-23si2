from auth import login
from user_service import register_user

def main():
    print("Welcome to User System")

    action = input("login/register: ").strip().lower()

    if action not in ["login", "register"]:
        print("unknown action. please choose 'login' or 'register'")
        return

    username = input("username: ").strip()
    password = input("password: ").strip()

    if not username or not password:
        print("username and password cannot be empty")
        return

    if action == "login":
        result = login(username, password)
        print(result)

    elif action == "register":
        try:
            register_user(username, password)
            print("user created successfully")
        except Exception as e:
            print(f"failed to create user: {e}")

if __name__ == "__main__":
    main()
