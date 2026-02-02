from auth import login
from user_service import register_user

def main():
    print("Welcome to User System")

    action = input("login/register: ").strip().lower()

    if action == "login":
        username = input("username: ")
        password = input("password: ")
        print(login(username, password))
    elif action == "register":
        username = input("username: ")
        password = input("password: ")
        register_user(username, password)
        print("user created")
    else:
        print("unknown action")

if __name__ == "__main__":
    main()
