from auth import login
from user_service import register_user

def main():
    print("Welcome to User System")

    action = input("login/register: ").strip()

    if action == "login":
        username = input("username: ").strip()
        password = input("password: ").strip()

        result = login(username, password)
        print(result)

    elif action == "register":
        username = input("username: ").strip()
        password = input("password: ").strip()

        register_user(username, password)
        print("User has been successfully created.")

    else:
        print("Invalid action. Please choose either 'login' or 'register'.")

if __name__ == "__main__":
    main()
