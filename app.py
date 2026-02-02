from auth import login
from user_service import register_user


MIN_PASSWORD_LENGTH = 6


def get_required_input(prompt: str) -> str:
    value = input(prompt).strip()
    if not value:
        print("Input cannot be empty.")
        return None
    return value


def get_valid_password() -> str:
    while True:
        password = input("Password: ").strip()

        if not password:
            print("Password cannot be empty.")
            continue

        if len(password) < MIN_PASSWORD_LENGTH:
            print(
                f"Password must be at least {MIN_PASSWORD_LENGTH} characters long."
            )
            continue

        return password


def main():
    print("=== Welcome to User System ===")

    action = input("Choose action (login/register): ").strip().lower()

    if action not in ("login", "register"):
        print("Invalid action. Please choose 'login' or 'register'.")
        return

    username = None
    while username is None:
        username = get_required_input("Username: ")

    password = get_valid_password()

    try:
        if action == "login":
            result = login(username, password)
            print(result)
        else:
            register_user(username, password)
            print("User successfully created.")

    except Exception:
        print("[System Error] Something went wrong. Please try again later.")


if __name__ == "__main__":
    main()
