# Modified by Vincent Liawis
from auth import login
from user_service import register_user

def show_menu():
    print("\n=== SYSTEM MANAGEMENT USER ===")
    print("1. Login ke Akun")
    print("2. Register Akun Baru")
    print("3. Keluar")
    return input("Pilih menu (1/2/3): ")

def main():
    while True:
        choice = show_menu()

        if choice == "1":
            u = input("Masukkan username: ")
            p = input("Masukkan password: ")
            result = login(u, p)
            print(f"Status: {result}")
        
        elif choice == "2":
            u = input("Daftarkan username: ")
            p = input("Daftarkan password: ")
            register_user(u, p)
            print(f"Berhasil! User '{u}' telah dibuat.")
        
        elif choice == "3":
            print("Terima kasih telah menggunakan sistem ini.")
            break
            
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    main()