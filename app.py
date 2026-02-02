from auth import login
from user_service import register_user

def main():
    print("Welcome to the User System!")

    action = input("Do you want to 'login' or 'register'? ").strip().lower()

    if action == "login":
        username = input("Enter your username: ").strip()
        password = input("Enter your password: ").strip()

        # Input validation
        if not username or not password:
            print("Error: Username and password cannot be empty.")
            return

        result = login(username, password)
        if result:
            print(f"Login successful! Welcome, {username}.")
        else:
            print("Error: Invalid username or password.")

    elif action == "register":
        username = input("Choose a username: ").strip()
        password = input("Choose a password: ").strip()

        # Input validation
        if not username or not password:
            print("Error: Username and password cannot be empty.")
            return

        try:
            register_user(username, password)
            print(f"User '{username}' has been successfully created.")
        except Exception as e:
            print(f"Error: Failed to create user. {str(e)}")

    else:
        print("Error: Unknown action. Please type 'login' or 'register'.")

if __name__ == "__main__":
    main()
