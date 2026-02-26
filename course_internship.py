from auth import login_required

#This is the parent class, that will pass traits via super() to another class
class BaseService:
    def __init__(self, service_name):
        self.service_name = service_name

#This is the child class that shall have the catalog of the courses and internship programs
class InternshipPortal(BaseService):
    def __init__(self, service_name, catalog_data):
      
        super().__init__(service_name)
        self.catalog = catalog_data
          # super() links this child class to the Parent (BaseService)


#we incoroporate our bouncer aka the decorator, 
# to ensure thecourses are shown if the login check was authenticated
    @login_required
    def show_courses(self):
        print(f"\n--- {self.service_name} ---")
        # we use self.catalog because the data is now encapsulated in the object
        #what we did in auth.py
        for key, course in self.catalog.items():
            print(f"{key}. {course['name']}")
        
        choice = input("Select your course number: ")
        
        if choice in self.catalog:
            self.show_programs(choice)
        else:
            print("Invalid selection.")

    def show_programs(self, course_key):
        course = self.catalog[course_key]
        print(f"\nPrograms in {course['name']}:")
        
        #we define the internship program list here
        program_list = course['programs']

        for i, program in enumerate(course['programs'], 1):
            print(f"{i}. {program}")
        
        prog_choice = input("Select a program number: ")
        
        try:
            index = int(prog_choice) - 1
            if 0 <= index < len(program_list):
                selected = program_list[index]
                print(f"\nSuccess! Application for '{selected}' Received.")
                print("We shall contact you via your email. Thank you.")
            else:
                print("\nError: That number is not on the list.")
        except ValueError:
            print("\nError: Please enter a valid number (e.g., 1, 2).")

# This is the global scope of the internship data in the program

catalog = {
    "1": {"name": "Software Engineering", "programs": ["Safaricom (Frontend Developer)", "NGC (Backend Developer)", "MoringaSchool (Technical Manager)"]},
    "2": {"name": "Business Management", "programs": ["Bidco (Financial Analyst)", "EABL (Project Manager)"]},
    "3": {"name": "Law", "programs": ["Karanja Law Firm (Intern)", "Sheria and Family Firm (Intern)"]},
    "4": {"name": "Hotel and Catering", "programs": ["Radisson Blu (Chef Intern)"]}
}

# 2. The object with its object attributes
portal = InternshipPortal("Available Courses", catalog)