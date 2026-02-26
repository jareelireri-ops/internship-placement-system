from auth import register_user, login_user
from course_internship import portal

def main():
    print("=== WELCOME TO LUCKY-YOU INTERNSHIP PORTAL ===")
    
    while True:
        # 1. The Menu Display
        print("\nMain Menu:")
        print("1. Register (New User)")
        print("2. Login (Existing User)")
        print("3. Exit")
        
        choice = input("Select an option (1-3): ")

       #Then the user selects a choice and the following conditions are run
       #this conditions are based on functions that we imported from auth.py and course_internship.py

        if choice == "1":
            register_user() 
            
        elif choice == "2":
            user = login_user() 
            if user:
                
                portal.show_courses()
                
        elif choice == "3":
            print("Thank you for using the portal. Goodbye!")
            break 
        # Breaks the 'while True' loop to close the program
            
        else:
            print("Invalid choice, please select 1, 2, or 3.")
        #anything else typed thats not in the choices, is considered invalid

#a basic standard of python of ensuring the system is run from main.py

# Run program
if __name__ == "__main__":
    main()