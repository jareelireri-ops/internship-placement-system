from colorama import Fore, Style, init

#we use the function below to ensure the colors work correctly in the os being used
init(autoreset=True)
from data_mgt import save_user, load_users

#first and forremost we create the class that shall contain all the user details
class User:
    def __init__(self, user_id, name, email, password):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password
#then we convert all the data collected into one box(capsule).This is enscapulation
#the to dict function enables the whole program to access the enscapulated data
    def to_dict(self):
    
        return {
            "name": self.name,
            "email": self.email,
            "password": self.password
        }

# The global session tracker, that starts the program with no users
current_user = None
#we create our decorator, that shall secure the contnents of our program  via requiring a valid login
def login_required(func):
    def wrapper(*args, **kwargs):
        if current_user is None:
            print(Fore.RED + Style.BRIGHT + "Access Denied: Please log in first.")
            return None
        return func(*args, **kwargs)
    return wrapper
#user is expected to register for their data to be recorded in the class
def register_user():
    print("\n--- Registration ---")
    name = input("Enter your full name: ")
    user_id = input("Enter your ID number: ")
    email = input("Enter your email: ")
    password = input("Create a password: ")
    
    existing_users = load_users()
    if user_id in existing_users:
        print(Fore.RED + Style.BRIGHT + "Error: A user with this ID already exists!")
        return False

    # the user class gets an instance
    new_user = User(user_id, name, email, password)
    
    # We call save_user to_dict() to get the data so we can store it
    save_user(new_user.user_id, new_user.to_dict())
    
    print(f"Welcome {new_user.name}. Your Account Has been created successfully!")
    return True

#once registered a user can log in
def login_user():
    global current_user
    print("\n--- Login ---")
    user_id = input("Enter your ID number: ")
    password = input("Enter your password: ")
    
    users = load_users()
    if user_id in users and users[user_id]["password"] == password:
        #we confirm if the Id number given is in users and if it matches the password aligned with it.
        user_data = users[user_id]

        print(f"Welcome back, {user_data['name']}!")
        
        # We store the active/current user as a dictionary for the rest of the app to use
        current_user = {"id": user_id, **user_data}
        return current_user
    else:
        print(Fore.RED + Style.BRIGHT + "Error: Invalid ID or Password.")
        return None