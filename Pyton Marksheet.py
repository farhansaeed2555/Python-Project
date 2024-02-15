# Function to calculate grade based on percentage
def calculate_grade(percentage):
    if percentage >= 90:
        return 'A+'
    elif 80 <= percentage < 90:
        return 'A'
    elif 70 <= percentage < 80:
        return 'B'
    elif 60 <= percentage < 70:
        return 'C'
    else:
        return 'D'

# List to store student information
students = []

# Input data for each student
for i in range(1, 11):
    print(f"\nStudent {i}:")
    name = input("Enter student name: ")
    total_subjects = int(input("Enter total subjects: "))
    
    # Input marks for each subject
    marks_obtained = 0
    for subject in range(1, total_subjects + 1):
        subject_marks = int(input(f"Enter marks for Subject {subject}: "))
        marks_obtained += subject_marks

    total_marks = total_subjects * 100  # Assuming each subject has 100 total marks
    percentage = (marks_obtained / total_marks) * 100
    grade = calculate_grade(percentage)

    # Add student information to the list
    students.append({
        'Name': name,
        'Marks Obtained': marks_obtained,
        'Total Marks': total_marks,
        'Percentage': percentage,
        'Grade': grade
    })

# Display mark sheets for all students
print("\nMark Sheets for Students:")
for student in students:
    print(f"\nName: {student['Name']}")
    print(f"Marks Obtained: {student['Marks Obtained']} out of {student['Total Marks']}")
    print(f"Percentage: {student['Percentage']}%")
    print(f"Grade: {student['Grade']}")
