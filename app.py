from auth import login
from user_service import register_user


def is_valid_input(value, field_name):
    if not value or not value.strip():
        print(f"Error: {field_name} cannot be empty")
        return False
    return True


def main():
    print("Welcome to User System")

    action = input("login/register: ").strip().lower()

    if action not in ("login", "register"):
        print("Error: action must be 'login' or 'register'")
        return

    if action == "login":
        u = input("username: ")
        p = input("password: ")

        if not is_valid_input(u, "username") or not is_valid_input(p, "password"):
            return

        print(login(u, p))

    elif action == "register":
        u = input("username: ")
        p = input("password: ")

        if not is_valid_input(u, "username") or not is_valid_input(p, "password"):
            return

        register_user(u, p)
        print("user created")


if __name__ == "__main__":
    main()
