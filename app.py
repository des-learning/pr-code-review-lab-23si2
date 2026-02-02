from auth import login
from user_service import register_user

def main():
    print("Welcome to User System")
    print("PR practice by Cariven Tan") 

    action = input("login/register: ")

    if action == "login":
        u = input("username: ")
        p = input("password: ")
        print(login(u, p))
    elif action == "register":
        u = input("username: ")
        p = input("password: ")
        register_user(u, p)
        print("user created")
    else:
        print("unknown action")

if __name__ == "__main__":
    main()
