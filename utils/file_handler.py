from utils.logger import log_activity
import os
from utils.encryption import encrypt_file , decrypt_file
import shutil

UPLOAD_FOLDER = "storage/uploads"

def upload_file(username):
    file_path = input("Enter the file path: ").strip()

    if not os.path.exists(file_path):
        print("File not found.")
        return
    
    encrypted_data = encrypt_file(file_path)
    filename = os.path.basename(file_path)

    save_path = os.path.join(
        "storage",
        "encrypted",
        f"{username}_{filename}.enc"

    )

    with open(save_path,"wb") as file:
        file.write(encrypted_data)
    
    log_activity(f"{username} uploaded {filename}")
    print("File encrypted and uploaded successfully.")
    
    filename = os.path.basename(file_path)
    destination = os.path.join(UPLOAD_FOLDER, filename)

    shutil.copy(file_path, destination)
    print("file uploaded successfully.")

def format_file_size(size):
     if size < 1024:
          return f"{size} B"
     elif size< 1024 *1024 :
          return f"{size / 1024 : .2f} KB"
     elif size< 1024 *1024 *1024 :
          return f"{size / (1024 * 1204) : .2f} MB"
     else:
          return f"{size / (1024 * 1024 * 1024): .2f}GB"


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
    
    decrypted_data = decrypt_file(encrypted_data)

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
            print(f"{i}.{file['name']} ({file['size']})")

     choice = int(input("\n Enter file number to restore: "))
     if choice < 1 or choice > len(files):
          print("Invalid Choice.")
          return
     selected_file = files[choice-1]["name"]

     source = os.path.join(recycle_bin, selected_file)

     destination = os.path.join(
          "storage",
          "encrypted",
          selected_file
     )
     if os.path.exists(destination):
          print("File already exists.")
          return
     shutil.move(source,destination)
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
     
     print("Deleted Files: ")
     for i, file in enumerate(files, start=1):
            print(f"{i}.{file['name']} ({file['size']})")
     
     choice = int(input("\n Enter file number to permanantly delete: "))
     if choice < 1 or choice > len(files):
          print("Invalid Choice")
          return
     selected_file = files[choice-1]["name"]

     confirm = input(f"Are you sure you want to permanantly delete '{selected_file}' (yes/no): ").lower()
     if confirm != "yes":
          print("Operation cancelled.")
          return
          
     file_path = os.path.join(recycle_bin,selected_file)
     os.remove(file_path)
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
         if keyword in file.lower():
                  matching_files.append(file)
     
     if not matching_files:
          print("No matching files found.")
          return
     print("\n Supporting results: ")

     for index,file in enumerate(matching_files,start=1):
            print(f"{index}.{file['name']} ({file['size']})")
        
     try :
         choice = int(input("Select file number: "))

         if choice < 1 or choice >len(user_files):
              print("Invalid file number.")
     except ValueError:
         print("Please enter valid number.")
         return
     
     file_name = user_files[choice-1]["name"]

     print(f"You selected: {file_name}")

def view_logs(username):
     print("\n ===== Activity Logs =====")

     try:
      with open("logs/activity.log","r") as file:
        found = False
        
        for line in file :
             if username in line:
                  print(line.strip())
                  found = True

        if not found:
             print("No activity found.")
             
     except FileNotFoundError:
      print("Activity log file not found.")
          
