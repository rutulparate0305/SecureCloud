from utils.logger import log_activity
from utils.file_handler import upload_file, download_file , delete_file, search_files, view_logs,restore_file,permanent_delete
import json 
import hashlib
import os
from utils.file_handler import(get_total_files,
                               get_storage_used,
                               get_recycle_count,
 )



USER_FILE = "users/users.json"

def register_user():
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    # Checking for existing users

    if os.path.exists(USER_FILE):
        with open(USER_FILE,"r") as file:
            try :
                users = json.load(file)
            except json.JSONDecodeError:
                users = {}
    else:
        users = {}
    
    # If user exists in the database
    
    if username in users:
        print("Username already exists.")
        return
    
    # Maintaining the password security by converting it into hashed code
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    users[username] = {
        "password" : hashed_password
    }

    with open (USER_FILE, "w") as file:
        json.dump(users , file, indent = 4)
    
    log_activity(f"{username} registered.")
    print("Registration succesfull.")
    


def login_user():
    username = input("Enter username : ").strip()
    password = input("Enter password : ").strip()

    if not os.path.exists(USER_FILE):
        print("No users registered.")
        return 
    
    with open(USER_FILE,"r") as file:
        users = json.load(file)

    if username not in users:
        print("Invalid username or passowrd")
        return
    
    # Maintaning password integrity after login by converting it to hashed pwd
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    
    
    if hashed_password == users[username]["password"]:
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

