from utils.logger import log_activity
from utils.file_handler import upload_file, download_file , delete_file, search_files, view_logs,restore_file,permanent_delete 
import hashlib
from utils.file_handler import(get_total_files,
                               get_storage_used,
                               get_recycle_count,
 )
from utils.database import add_user, get_user


def register_user():
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()
    
    # If user exists in the database
    if get_user(username):
        print("Username already exists.")
        return
    
    # Maintaining the password security by converting it into hashed code
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    add_user(username,hashed_password) 
    print("Registration successfull")
    
    log_activity(f"{username} registered.")    


def login_user():
    username = input("Enter username : ").strip()
    password = input("Enter password : ").strip()
    user = get_user(username)

    if not user:
        print("Invalid username or passowrd")
        return
    
    # Maintaning password integrity after login by converting it to hashed pwd
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    
    stored_password = user[2] 
    if hashed_password == stored_password:
        log_activity(f"{username} logged in")
        print(f"\n Welcome, {username}")
        print("\n ====== DASHBOARD ======")
        print(f"Files Stored        :   {get_total_files(username)}")
        print(f"Storage Used        :  {get_storage_used(username)}")
        print(f"Recycle Bin Files   :   {get_recycle_count(username)}")
        print("=" *25)
    
        
        while True:
            print("\n ====== USER MENU ======")
            print("1. Upload File")
            print("2. Download File")
            print("3. Delete File")
            print("4. Restore File")
            print("5. Search File")
            print("6. Permanant Delete File")
            print("7. View Activity logs")
            print("8. Logout")

            choice = input("Enter your choice: ")

            if choice == "1":
                upload_file(username)
            elif choice == "2":
                download_file(username)
            elif choice == "3" :
                delete_file(username)
            elif choice == "4":
                restore_file(username)
            elif choice == "5":
                search_files(username)
            elif choice =="6":
                permanent_delete(username)
            elif choice =="7":
                view_logs(username)
            elif choice =="8":
                break

               
            
            else:
                print("Invalid Choice.")
    else:
        print("Invalid username or password")

