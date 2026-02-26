import json
import os

DB_FILE = "users.json"

def initialize_db():
    #first, we check if the database file exists,if not it is created.
    if not os.path.exists(DB_FILE):
        with open(DB_FILE, "w") as f:
            json.dump({}, f)
        print(f"--- System: Initialized new database at {DB_FILE} ---")

def load_users():
    
    initialize_db() #we ensure the file exists before reading
    with open(DB_FILE, "r") as f:
        return json.load(f)

def save_user(user_id, user_data):
   #first we get the existing data
    all_users = load_users() 

    #then we get the new entry and values using the key(user_id)
    
    all_users[user_id] = user_data 
    with open(DB_FILE, "w") as f:
        json.dump(all_users, f, indent=4)