student_marks = {"Alice": 1, "Bob": 2, "Charlie": 3, "Neil": 3}

student_name = input("Enter the student's name: ")

marks = student_marks.get(student_name)

if marks is not None:
    print(f"{student_name}'s marks: {marks}")
else:
    print("Student not found")