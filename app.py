from auth import login
from user_service import register_user

def validate_input(username, password):
    """Validate username and password input"""
    errors = []
    
    if not username or not password:
        errors.append("Username dan password tidak boleh kosong")
    
    if username and ' ' in username:
        errors.append("Username tidak boleh mengandung spasi")
    
    if username and len(username) < 3:
        errors.append("Username minimal 3 karakter")
    
    if password and len(password) < 6:
        errors.append("Password minimal 6 karakter")
    
    return errors

def main():
    print("Welcome to User System")
    action = input("login/register: ").strip().lower()
    
    if action == "login":
        u = input("username: ").strip()
        p = input("password: ").strip()
        
        errors = validate_input(u, p)
        if errors:
            for error in errors:
                print(f"Error: {error}")
            return
        
        print(login(u, p))
        
    elif action == "register":
        u = input("username: ").strip()
        p = input("password: ").strip()
        
        errors = validate_input(u, p)
        if errors:
            for error in errors:
                print(f"Error: {error}")
            return
        
        register_user(u, p)
        print("user created")
        
    else:
        print("unknown action")

if __name__ == "__main__":
    main()