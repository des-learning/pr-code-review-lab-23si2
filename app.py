from auth import login
from user_service import register_user

def main():
    print("Welcome to User System")

    action = input("login/register: ").strip()

    if action not in ["login", "register"]:
        print("Invalid action. Please choose 'login' or 'register'.")
        return

    username = input("username: ").strip()
    password = input("password: ").strip()

    if not username or not password:
        print("Username and password cannot be empty.")
        return

    if action == "login":
        print(login(username, password))
    else:
        register_user(username, password)
        print("User created successfully.")

if __name__ == "__main__":
    main()
