# Import json module to store data persistently
import json

# Import hashlib for password hashing (security)
import hashlib

# Import random to randomly assign a company
import random

# File where student data will be stored
DATA_FILE = "students.json"


#Helper functions(for file storage)
def load_students():
    # Trying to open the JSON file
    try:
        with open (DATA_FILE, "r") as file:     #opens a file in read mode
            return json.load(file)     #it converts  JSON to pyhton list
    except FileNotFoundError:
        return []       # if file doesn't exist, it returns an empty list
   
   
def save_students(students):
       with open (DATA_FILE, "w") as file:   #opens file in write mode
           json.dump(students, file, indent=4)   #saves python as JSON into a file
           

#user class, encapsulation
class User:
    """
    Base class for all users.
    Demonstrates encapsulation of password.
    """
 
    def __init__(self, username, password):
        self.username = username
        
    #using a private password ,encapsulation
        self._password = self.hash_password(password)
        
    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()   #converts password into secure hash
    
    def verify_password(self,password):
        return self._password == self.hash_password(password)  #compares entered password with stored hashed password
    
    def get_password(self):
        return self._password


#student class, inheritance
class Student(User):
    """
    Student inherits from User.
    Demonstrates inheritance.
    """
        
    def __init__(self, username, password):
        super().__init__(username, password)     #calling parent constructor
        
        #specific attributes
        self.course = None
        self.company = None
            

    # Method to select program
    def select_course(self):

        print("\nAvailable Programs: ")
        print("1. Software Engineering")
        print("2. Data Science")
        print("3. Business")
        print("4. Medicine")
        print("5. Cyber Security")
        print("6. Artificial Intelligence")

        choice = input("Select program number: ")

        # Assign course based on user choice
        if choice == "1":
            self.course = "Software Engineering"
        elif choice == "2":
            self.course = "Data Science"
        elif choice == "3":
            self.course = "Business"
        elif choice == "4":
            self.course = "Medicine"
        elif choice == "5":
            self.course = "Cyber Security"
        elif choice == "6":
            self.course = "Artificial Intelligence"
        else:
            print("Invalid choice.")
            return

        # After choosing program, assign company
        self.assign_company()

    # Method to assign company automatically
    def assign_company(self):

        companies = {
            "Software Engineering": ["TechCorp", "DevSolutions"],
            "Data Science": ["DataLabs", "InsightAnalytics"],
            "Business": ["BizGroup", "MarketLeaders"],
            "Medicine": ["City Hospital", "HealthCare Plus"],
            "Cyber Security": ["SecureIT", "CyberShield"],
            "Artificial Intelligence": ["AIBrain", "FutureTech"]
        }

    # Randomly choose company based on course
        self.company = random.choice(companies[self.course])
        print(f"\nYou have been placed at {self.company} under {self.course}.")

    
    # method for viewing internship details
    def view_details(self):
        print("\n-------Internship Details------")
        print("Username:", self.username)
        print("Program:", self.course)
        print("Company", self.company)


#registration function
def register():

    students = load_students()  # Load saved students

    username = input("Enter username: ")
    password = input("Enter password: ")

    # Check if username already exists
    for student in students:
        if student["username"] == username:
            print("Username already exists!")
            return

    # Create Student object
    new_student = Student(username, password)

    # Save student info into dictionary
    students.append({
        "username": new_student.username,
        "password": new_student.get_password(),
        "course": new_student.course,
        "company": new_student.company
    })

    save_students(students)  # Save to JSON file

    print("Registration successful!")



#login function


def login():

    students = load_students()

    username = input("Enter username: ")
    password = input("Enter password: ")

    # Loop through saved students
    for student_data in students:

        if student_data["username"] == username:

            # Create temporary student object
            temp_student = Student(username, password)

            # Replace private password with stored hashed password
            temp_student._User__password = student_data["password"]

            # Verify password
            if temp_student.verify_password(password):

                # Restore saved course and company
                temp_student.course = student_data["course"]
                temp_student.company = student_data["company"]

                print("Login successful!")

                return temp_student

    print("Invalid credentials.")
    return None



# updating student data


def update_student_data(student):

    students = load_students()

    # Update matching student record
    for s in students:
        if s["username"] == student.username:
            s["course"] = student.course
            s["company"] = student.company

    save_students(students)



def main():

    current_user = None  # No user logged in at start

    while True:

        # If no user logged in
        if not current_user:

            print("\n1. Register")
            print("2. Login")
            print("3. Exit")

            choice = input("Choose option: ")

            if choice == "1":
                register()

            elif choice == "2":
                current_user = login()

            elif choice == "3":
                print("Goodbye!")
                break

        # If user is logged in
        else:

            print("\n1. Select Program")
            print("2. View Internship Details")
            print("3. Logout")

            choice = input("Choose option: ")

            if choice == "1":
                current_user.select_course()
                update_student_data(current_user)

            elif choice == "2":
                current_user.view_details()

            elif choice == "3":
                print("Logged out successfully.")
                current_user = None


# Run program
if __name__ == "__main__":
    main()

