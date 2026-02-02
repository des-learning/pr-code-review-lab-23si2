from auth import login
from user_service import register_user


def get_non_empty_input(login1):
    """user until non-empty input is given."""
    while True:
        value = input(login1).strip()
        if not value:
            print("Input cannot be empty. Please try again.")
        else:
            return value


def get_valid_password():
    """ user until password meets minimum requirements."""
    while True:
        password = input("Password: ").strip()
        if len(password) < 6:
            print("Password must be at least 6 characters long.")
        else:
            return password


def main():
    print("=== Welcome to User System ===")

    user_action = input("Do you want to login or register? ").strip().lower()

    if user_action == "login":
        username = get_non_empty_input("Username: ")
        password = get_valid_password()

        try:
            result = login(username, password)
            print(f"Login result: {result}")
        except Exception as e:
            print(f"An error occurred during login: {e}")

    elif user_action == "register":
        username = get_non_empty_input("Username: ")
        password = get_valid_password()

        try:
            register_user(username, password)
            print("User successfully created.")
        except Exception as e:
            print(f"An error occurred during registration: {e}")

    else:
        print("Invalid action. Please type 'login' or 'register'.")


if __name__ == "__main__":
    main()
