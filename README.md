: Student Internship Portal (LUCKY YOU)
A simple Python program for students to sign up, log in, and apply for internship positions.

: What’s in the Folder?
main.py – The main menu. Start the program from here.

auth.py – The "Bouncer." Handles sign-ups and makes sure only logged-in users can see the internships.

course_internship.py – The List. Contains all the courses (Software, Law, etc.) and their specific internship spots.

data_mgt.py – The Saver. Handles saving and loading your information so it doesn't disappear when you close the app.

users.json – The Storage. This is where your account details are kept.

: How to Run
Install the Color Tool:
Open your terminal and type:

Bash
pip install colorama
Start the App:
Type:

Bash
python main.py
:
 What it Does
Remembers You: When you create an account, it saves it to a file. You can close the app, come back later, and your login will still work.

Locked Doors: You can't see the internship list unless you are logged in. The "Bouncer" code blocks anyone else.

Smart Lists: The internships are organized by category, so it's easy to find what fits your course.

Colorful Alerts: If you make a mistake (like a wrong password), the error message pops up in Bold Red so you can't miss it.

Built with Python 3 and Colorama.