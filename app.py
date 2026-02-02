from auth import login
from user_service import register_user

def main():
    print("Welcome to User System")
    
    try:
        action = input("login/register: ").strip().lower()
        
        if action == "login":
            username = input("username: ").strip()
            password = input("password: ").strip()
            
            if not username or not password:
                print("Username dan password harus diisi!")
                return
                
            print(login(username, password))
            
        elif action == "register":
            username = input("username: ").strip()
            password = input("password: ").strip()
            
            if not username or not password:
                print("Username dan password harus diisi!")
                return
            
            if len(password) < 6:
                print("Password minimal 6 karakter!")
                return
                
            register_user(username, password)
            print("user created")
        else:
            print("unknown action")
            
    except KeyboardInterrupt:
        print("\nProgram dihentikan")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()