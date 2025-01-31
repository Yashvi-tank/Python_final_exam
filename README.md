Overview:
A web application integrating Django backend and Flask frontend to manage and display student information and grades.

Features:

Django Backend API for student, subject, and grade data management
Flask Frontend dashboard with student names and grade averages
Full CRUD operations for student records
REST API integration
Dynamic and organized student data presentation

Tech Stack:

Backend: Django, Django REST Framework
Frontend: Flask, HTML, CSS
Database: SQLite

Installation:
Django Backend Setup:
1. Install dependencies:
pip install django djangorestframework

2. Run migrations:
python manage.py migrate

3. Start Django server:
python manage.py runserver
(At http://127.0.0.1:8000/)

Flask Frontend Setup:
1. Install dependencies:
pip install flask requests

2. Run Flask app:
python app.py
(at http://127.0.0.1:5000/)

Troubleshooting:

Ensure Django server is running at http://127.0.0.1:8000/
Verify API endpoints return valid JSON
Check static folder references in HTML


Credentials for login:
Username: yashvi
Password: abcd

API Endpoints:

GET /stu/ - Retrieve all students
POST /stu/ - Create a new student
GET /stu/<id>/ - Retrieve specific student
PUT /stu/<id>/ - Update a student
DELETE /stu/<id>/ - Delete a student
GET /sub/ - Retrieve all subjects
POST /sub/ - Create a new subject
GET /gra/ - Retrieve all grades
POST /gra/ - Create a new grade

Credits:
Yashvi TANK & Jesica KARDOS