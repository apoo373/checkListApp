This project has been designed in python-django v1.11 (python v2.7)

Follow the steps to run the project:
1) Install python2.7 and django
- pip install django
2) Extract the zip file and go inside signzy folder
- tar -xvf singzy_assignment_apoorva.tar
- cd signzy
3) Run the server 
- python manage.py runserver
4) Go to Browser and go to (http://127.0.0.1:8000/admin/)
- The default admin of django is used to provide a lot more flexiblity while testing
- You can use the Admin to create and manage users (and CheckList Items as well) as a sort of verification.
- You can create your own superusers (one has been created for you)
- username: apoorva
- password: apoorva123
5) After login, go to http://127.0.0.1:8000/account/dashboard)
- You shall see all the Items created by the concerned user (sorted according to priority)
- You can view individual Item and modify them as needed (Or Delete them)
- Options include 
	a) Editing All Relevant Fields of Item
	b) Marking it as completed / Reactivating them
	c) Outright deleting them
- You can create a new Item also (Option avalaible in the sidebar)
6) All the above API calls are authentication-enforced, meaning you cannot individually call them without logging in.
7) None of the above mentioned operation can be performed for any item not created by the concerned user.
8) All the pages of the Checklist Application has been styled with bootstrap (although unpolished due to time constraints)
9) Finally, Logout is also available on sidebar.
