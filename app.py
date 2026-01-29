from auth import login
from user_service import register_user
from utils import is_empty

def main():
    print("Welcome to User System")

    action = input("login/register: ").lower()

    if action == "login":
        username = input("username: ")
        password = input("password: ")

        if is_empty(username) or is_empty(password):
            print("Username dan password tidak boleh kosong")
            return

        print(login(username, password))

    elif action == "register":
        username = input("username: ")
        password = input("password: ")

        if is_empty(username) or is_empty(password):
            print("Username dan password tidak boleh kosong")
            return

        if register_user(username, password):
            print("User created")
        else:
            print("User already exists")

    else:
        print("Unknown action")

if __name__ == "__main__":
    main()
