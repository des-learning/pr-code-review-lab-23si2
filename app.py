from auth import login
from user_service import register_user

def main():
    print("Welcome to User System")

    # Ask user for action: login or register
    action = input("login/register: ").strip().lower()

    if action == "login":
        username = input("username: ").strip()
        password = input("password: ").strip()
        print(login(username, password))
    elif action == "register":
        username = input("username: ").strip()
        password = input("password: ").strip()
        result = register_user(username, password)
        print(result)
    else:
        print("Unknown action. Please type 'login' or 'register'.")

if __name__ == "__main__":
    main()
