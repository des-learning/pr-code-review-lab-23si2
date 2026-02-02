from auth import login
from user_service import register_user

def is_valid_input(username, password):
    if not username.strip():
        print("Error: username cannot be empty")
        return False

    if not password.strip():
        print("Error: password cannot be empty")
        return False

    if len(password) < 6:
        print("Error: password must be at least 6 characters")
        return False

    return True


def main():
    print("Welcome to User System")

    action = input("login/register: ").strip()

    if action == "login":
        u = input("username: ")
        p = input("password: ")

        if not is_valid_input(u, p):
            return

        print(login(u, p))

    elif action == "register":
        u = input("username: ")
        p = input("password: ")

        if not is_valid_input(u, p):
            return

        register_user(u, p)
        print("user created")

    else:
        print("unknown action")


if __name__ == "__main__":
    main()
