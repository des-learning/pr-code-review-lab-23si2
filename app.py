from auth import login
from user_service import register_user


def get_input(prompt: str) -> str:
    """
    Helper untuk mengambil input dan memastikan tidak kosong.
    """
    value = input(prompt).strip()
    if not value:
        raise ValueError("Input tidak boleh kosong")
    return value


def main():
    print("Welcome to User System")

    try:
        action = get_input("login/register: ").lower()

        if action == "login":
            username = get_input("username: ")
            password = get_input("password: ")
            result = login(username, password)
            print(result)

        elif action == "register":
            username = get_input("username: ")
            password = get_input("password: ")
            register_user(username, password)
            print("User created successfully")

        else:
            print("Unknown action. Please choose 'login' or 'register'.")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
