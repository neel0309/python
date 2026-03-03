student_marks = {"Alice": 1, "Bob": 2, "Charlie": 3,"Neil": 3}


student_name = input(f"Enter the student's name:")

if student_name in student_marks:
    print(f"{student_name} marks: {student_marks[student_name]}")
else:
    print(f"{student_name} student not found")

