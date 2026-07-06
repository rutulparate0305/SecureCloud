
from utils.encryption import generate_key
from utils.auth import register_user, login_user


def main():
    
    generate_key()
    
    while True: 
     print("=" * 35)
     print("     Secure Cloud Storage")
     print("=" * 35)


     print("1. Register")
     print("2. Login")
     print("3. Exit")

     choice = input("\n Enter your choice: ")

     if choice == "1":
        register_user()

     elif choice == "2":
        login_user()

     elif choice == "3":
        print("\n Thank you for using Secure Cloud Storage.")
        break
     
     else:
        print("\n Invalid choice. Please try again.")

if __name__=="__main__":
   main()
    

# Now ... Its time run run ....