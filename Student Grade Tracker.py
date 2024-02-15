# Part a: Develop a system for tracking student grades
student = []

#Partv b: Utilize a list to store student names 
student_names = ["Saad", "Farhan", "Daniyal", "Maaz", "Faraz"]

# Part d: Employ a dicitionary to store additional informtion about each student 
student_info = {
    "Saad": {"contact_info": "saad@gmail.com", "attendance": 90},
    "Farhan": {"contact_info": "farhan@gmail.com", "attendance": 95},
    "Daniyal": {"contact_info": "daniyal@gmail.com", "attendance": 85},
    "Maaz": {"contact_info": "maaz@gmail.com", "attendance": 92},
    "Faraz": {"contact_info": "faraz@gmail.com", "attendance": 88},
}

# Part c: Use loops for inputting and updating grades
for student_name in student_names:
    # Assuming grades are input interactively
    grades = []
    for i in range(3):  # Assuming 3 subjects
        grade = float(input(f"Enter {student_name}'s grade for subject {i + 1}: "))
        grades.append(grade)
    # Update student info with grades 
    student_info[student_name]["grades"] = grades

# Display student information
for student_name, info in student_info.items():
    print(f"Student: {student_name}")
    print(f"Contact info: {info['contact_info']}")
    print(f"Attendance: {info['attendance']}%")
    if "grades" in info:
        print(f"Grades: {info['grades']}")
    print("----------------------")