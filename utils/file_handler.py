from utils.database import add_file_metadata, delete_file_metadata, update_file_status, get_user_key
import hashlib
from datetime import datetime
from utils.logger import log_activity
import os
from utils.encryption import encrypt_file , decrypt_file
import shutil


def upload_file(username):
    file_path = input("Enter the file path: ").strip()

    if not os.path.exists(file_path):
        print("File not found.")
        return
    
    key = get_user_key(username)
    if key is None:
         print("Encryption key not found.")
         return
        
    encrypted_data = encrypt_file(file_path,key)

    filename = os.path.basename(file_path)

    save_path = os.path.join(
        "storage",
        "encrypted",
        f"{username}_{filename}.enc"
    )

    with open(save_path,"wb") as file:
        file.write(encrypted_data)
    
    file_size = os.path.getsize(save_path)
    uploaded_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(save_path,"rb") as f:
         checksum = hashlib.sha256(f.read()).hexdigest()

    add_file_metadata(
         owner = username,
         original_name=filename,
         stored_name=f"{username}_{filename}.enc",
         file_size=file_size,
         uploaded_at=uploaded_at,
         checksum=checksum,
         status = "active"
     )
    
    log_activity(f"{username} uploaded {filename}")
    print("File encrypted and uploaded successfully.")


def format_file_size(size):
     if size < 1024:
          return f"{size} B"
     elif size < 1024 *1024 :
          return f"{size / 1024 :.2f} KB"
     elif size< 1024 *1024 *1024 :
          return f"{size / (1024 * 1204) :.2f} MB"
     else:
          return f"{size / (1024 * 1024 * 1024): .2f} GB"


def get_storage_used(username):
     total_size = 0

     for file in os.listdir("storage/encrypted"):
          if file.startswith(f"{username}_") :
            file_path = os.path.join("storage","encrypted",file)
            total_size += os.path.getsize(file_path)

     return format_file_size(total_size)

def get_total_files(username):
     count = 0

     for file in os.listdir("storage/encrypted"):
          if file.startswith(f"{username}_") :
               count+= 1
     
     return count

def get_recycle_count(username):
     recycle_bin = os.path.join("storage","recycle_bin", username)
     if not os.path.exists(recycle_bin):
          return 0
     
     files = [
          file for file in os.listdir(recycle_bin)
          if file != ".gitkeep"
     ]
     return len(files)
          

def get_user_files(username):
     files = os.listdir("storage/encrypted")
     user_files = []

     for file in files:
        if file.startswith(f"{username}_"):
            full_path = os.path.join("storage", "encrypted", file)
            size = os.path.getsize(full_path)
            original_name = file.replace(f"{username}_" , "").replace(".enc" ,"")
            user_files.append({
                 "name" : original_name,
                 "size" : format_file_size(size)
             })

     return user_files 
          

def download_file(username):
    print("\n Your Files: ")
    user_files = get_user_files(username)

    if not user_files:
            print("No uploads found in the directory")
            return
        
    for index,file in enumerate(user_files,start=1):
            print(f"{index}.{file['name']} ({file['size']})")
            
    try :
         choice = int(input("Select file number: "))

         if choice < 1 or choice >len(user_files):
              print("Invalid file number.")
    except ValueError:
         print("Please enter valid number.")
         return
    

    file_name = user_files[choice-1]["name"]

    encrypted_path = os.path.join(
        "storage",
        "encrypted",
        f"{username}_{file_name}.enc"
    )
    
    if not os.path.exists(encrypted_path):
         print("Encyrypted file not found")
         return
    
    with open(encrypted_path,"rb") as file:
        encrypted_data = file.read()
    
    key = get_user_key(username)
    if key is None:
         print("Encryption key not found.")
         return
    
    decrypted_data = decrypt_file(encrypted_data,key)

    download_path = os.path.join(
        "storage",
        "downloads",
        file_name
    )

    with open (download_path,"wb") as file:
        file.write(decrypted_data)
    log_activity(f"{username} downloaded {file_name}")
    print("File downlaoded and decrypted succesfully.")

def restore_file(username):
     recycle_bin = os.path.join("storage","recycle_bin",username)

     if not os.path.exists(recycle_bin):
          print("Recycle bin is empty.")
          return
     
     files = os.listdir(recycle_bin)

     if not files:
          print("Recycle bin is empty")
          return
     
     print("\n Deleted files: ")

     for i, file in enumerate(files, start = 1):
            file_path = os.path.join(recycle_bin,file)
            file_size = os.path.getsize(file_path)
            print(f"{i} . {file} ({format_file_size(file_size)})")

     try:
        choice = int(input("\n Enter the file number to restore: "))
     except ValueError:
         print("invalid input.")
         return
     

     if choice < 1 or choice > len(files):
          print("Invalid Choice.")
          return
     
     selected_file = files[choice-1]

     source = os.path.join(recycle_bin, selected_file)

     destination = os.path.join(
          "storage",
          "encrypted",
          selected_file
     )
     
     shutil.move(source,destination)
     update_file_status(selected_file,"active")
     log_activity(f"{username} restored {selected_file}")
     print("File restored successfully.")


def permanent_delete(username):
     recycle_bin = os.path.join("storage", "recycle_bin", username)

     if not os.path.exists(recycle_bin):
          print("recycle bin is empty.")
          return
     
     files = os.listdir(recycle_bin)

     if not files:
          print("Recycle bin is empty.")
          return
     
     print("\nDeleted Files: ")

     for i, file in enumerate(files, start=1):
            file_path = os.path.join(recycle_bin,file)
            print(f"{i}. {file} ({format_file_size(os.path.getsize(file_path))}) ")

     try:
        choice = int(input("\n Enter file number to permanantly delete: "))
     except ValueError:
          print("Invalid input.")
          return
     

     if choice < 1 or choice > len(files):
          print("Invalid Choice")
          return
     
     selected_file = files[choice-1]

     confirm = input(f"Are you sure you want to permanantly delete '{selected_file}' (yes/no): ").lower()
     if confirm != "yes":
          print("Operation cancelled.")
          return
          
     file_path = os.path.join(recycle_bin,selected_file)
     os.remove(file_path)
     delete_file_metadata(selected_file)

     log_activity(f"{username} permanantly deleted {selected_file}")
     print("File deleted permanantly successfully.")


def delete_file(username):
    print("\n Your Files: ")
    user_files = get_user_files(username)

    if not user_files:
            print("No uploads found in the directory")
            return
        
    for index,file in enumerate(user_files,start=1):
            print(f"{index}.{file['name']} ({file['size']})")
            
    try :
         choice = int(input("Select file number: "))

         if choice < 1 or choice >len(user_files):
              print("Invalid file number.")
    except ValueError:
         print("Please enter valid number.")
         return
    
    file_name = user_files[choice-1]["name"]

    
    encrypted_path = os.path.join(
        "storage",
        "encrypted",
        f"{username}_{file_name}.enc"
    )

    recycle_bin = os.path.join("storage","recycle_bin", username)
    os.makedirs(recycle_bin,exist_ok=True)

    destination = os.path.join(
         recycle_bin,
         os.path.basename(encrypted_path)
    )
     
    if not os.path.exists(encrypted_path):
         print("Encyrypted file not found")
         return
     
    shutil.move(encrypted_path, destination)
    update_file_status(f"{username}_{file_name}.enc","deleted")
    log_activity(f"{username} deleted {file_name}")
    print("File moved to recycle bin successfully")
    
def search_files(username):
     print("\n Search your file here")

     user_files = get_user_files(username)

     if not user_files:
        print("No file found.")
        return
     
     keyword = input("Enter file name or keyword: ").strip().lower()
     matching_files = []

     for file in user_files:
         if keyword in file["name"].lower():
                  matching_files.append(file)
     
     if not matching_files:
          print("No matching files found.")
          return
     
     print("\n Supporting results: ")

     for index,file in enumerate(matching_files,start=1):
            print(f"{index}.{file['name']} ({file['size']})")
        
     try :
         choice = int(input("Select file number: "))

     except ValueError:
         print("Invalid Input")
         return
     
     if choice < 1 or choice > len(matching_files):
          print("Invalid file number.")
          return 
     
     file_name = matching_files[choice-1]["name"]

     print(f"You selected: {file_name}")

def view_logs(username):
     print(f"Current username = {username}")
     print("\n ===== Activity Logs =====")

     try:
      with open("logs/activity.log","r") as file:
        found = False
        
        for line in file :
             parts = line.split(" - ", 1)

             if len(parts) > 1:
                  log_text = parts[1]
                  if log_text.startswith(username + " "):
                       print(line.strip())
                       found = True

        if not found:
             print("No activity found.")
             
     except FileNotFoundError:
      print("Activity log file not found.")
          
