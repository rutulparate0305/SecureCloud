from cryptography.fernet import Fernet
import os

KEY_FILE = "keys/secret.key"

def generate_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()

        
        with open(KEY_FILE, "wb") as file:
            file.write(key)

        print("Encryption key generated.")

    else:
        print("Key already exists.")

def load_key():
    with open(KEY_FILE,"rb") as file:
        return file.read()
    
def encrypt_file(file_path):
    key = load_key()
    fernet = Fernet(key)

    with open(file_path,"rb") as file:
        data = file.read()

    encrypted_data = fernet.encrypt(data)

    return encrypted_data

def decrypt_file(encrypted_data):
    with open(KEY_FILE,"rb") as file :
        key = file.read()

    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data)

    return decrypted_data