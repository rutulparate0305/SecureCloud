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

def get_user_files(username):
     files = os.listdir("storage/encrypted")
     user_files = []

     for file in files:
        if file.startswith(f"{username}_"):
            original_name = file.replace(f"{username}_" , "").replace(".enc" ,"")
            user_files.append(original_name)

     return user_files 
          

def download_file(username):
    print("\n Your Files: ")
    user_files = get_user_files(username)

    if not user_files:
            print("No uploads found in the directory")
            return
        
    for index,file in enumerate(user_files,start=1):
            print(f"{index}.{file}")
            
    try :
         choice = int(input("Select file number: "))

         if choice < 1 or choice >len(user_files):
              print("Invalid file number.")
    except ValueError:
         print("Please enter valid number.")
         return
    

    file_name = user_files[choice-1]

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

def delete_file(username):
    print("\n Your Files: ")
    user_files = get_user_files(username)

            

    if not user_files:
            print("No uploads found in the directory")
            return
        
    for index,file in enumerate(user_files,start=1):
            print(f"{index}.{file}")
            
    try :
         choice = int(input("Select file number: "))

         if choice < 1 or choice >len(user_files):
              print("Invalid file number.")
    except ValueError:
         print("Please enter valid number.")
         return
    
    file_name = user_files[choice-1]

    
    encrypted_path = os.path.join(
        "storage",
        "encrypted",
        f"{username}_{file_name}.enc"
    )
     
    if not os.path.exists(encrypted_path):
         print("Encyrypted file not found")
         return
    
    os.remove(encrypted_path)
    log_activity(f"{username} deleted {file_name}")
    print("File deleted successfully")
    
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
      print(f"{index}.{file}")
        
     try :
         choice = int(input("Select file number: "))

         if choice < 1 or choice >len(user_files):
              print("Invalid file number.")
     except ValueError:
         print("Please enter valid number.")
         return
     
     file_name = user_files[choice-1]

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
          

