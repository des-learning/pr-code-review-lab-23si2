from auth import login
from user_service import register_user


def main():
    print("Welcome to User System")

    action = input("login/register: ").strip().lower()

    if action == "login":
        username = input("username: ").strip()
        password = input("password: ").strip()

        result = login(username, password)
        print(result)

    elif action == "register":
        username = input("username: ").strip()
        password = input("password: ").strip()

        user = register_user(username, password)

        if user:
            print("user created")
        else:
            print("failed to create user")

    else:
        print("unknown action")


if __name__ == "__main__":
    main()