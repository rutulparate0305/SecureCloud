from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrypt_file(file_path,key):
    cipher = Fernet(key)

    with open(file_path,"rb") as file:
        data = file.read()

    return cipher.encrypt(data)

def decrypt_file(encrypted_data,key):

    cipher = Fernet(key)
    return cipher.decrypt(encrypted_data)