from flask import Flask, render_template  
import requests  

app = Flask(__name__)  

API_BASE_URL = "http://127.0.0.1:8000"

@app.route('/')
def dashboard():
    students = requests.get(f"{API_BASE_URL}/stu/").json()
    subjects = requests.get(f"{API_BASE_URL}/sub/").json()
    grades = requests.get(f"{API_BASE_URL}/gra/").json()

    # Ensuring validity of data
    if not isinstance(students, list) or not isinstance(subjects, list) or not isinstance(grades, list):
        return "Error: API did not return valid data", 500

    
    student_grades = {student['id']: [] for student in students}

    # Looping through grades and storing them correctly
    for grade in grades:  # Fixed incorrect variable reference
        student_id = grade.get('student')  # Ensuring key exists
        if student_id in student_grades:
            student_grades[student_id].append(grade.get('grade', 0))  

    # Computing student averages 
    averages = {
        student_id: sum(grades) / len(grades) if grades else 0
        for student_id, grades in student_grades.items()
    }

    # Constructing student data for rendering
    student_data = [
        {"name": next((s['name'] for s in students if s['id'] == student_id), "Unknown"),
         "average": average}
        for student_id, average in averages.items()
    ]

    return render_template("dashboard.html", students=student_data, subjects=subjects)  # Fixed correct rendering

if __name__ == "__main__":
    app.run(debug=True)
