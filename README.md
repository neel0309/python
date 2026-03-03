# Dictionary

# Create a Dictionary
student_marks = {"Alice": 1, "Bob": 2, "Charlie": 3, "Neil": 3}

A dictionary stores key-value pairs

Key → Student name

Value → Marks

Example:

"Alice" → 1

"Bob" → 2

# Take User Input
student_name = input("Enter the student's name:")

The user enters a student's name.

The input is stored in the variable student_name.

# Check If Student Exists

if student_name in student_marks:

The in operator checks whether the name exists as a key in the dictionary.

If found → display marks.

If not found → display "student not found".

# Display Result

print(f"{student_name} marks: {student_marks[student_name]}")

Uses f-strings for formatted output.

Accesses marks using dictionary key lookup.

If not found:

print(f"{student_name} student not found")

# Example Runs

When Student Exists
Enter the student's name: Alice
Alice marks: 1

When Student Does Not Exist
Enter the student's name: David
David student not found

Test Case 1 (Valid Name)
Enter the student's name: Alice
Alice marks: 1

Test Case 2 (Invalid Name)
Enter the student's name: David
David student not found

Test Case 3 (Another Valid Name)
Enter the student's name: Neil
Neil marks: 3


# Slice

# Create a List Using range()
original_list = list(range(1, 11))

range(1, 11) generates numbers from 1 to 10

list() converts the range into a list

Result:

[1,2,3,4,5,6,7,8,9,10]

# Extract the First Five Elements
extract = original_list[:5]

[:5] is list slicing

It selects elements from index 0 to 4

Result:

[1,2,3,4,5]


# Reverse Using Slicing [::-1]

reversed_list = extract[::-1]

:: → slicing operator

-1 → step backwards

Creates a new reversed list

Result:

[5,4,3,2,1]

# Print the Results
print(f"Original list: {original_list}")
print(f"Extracted first five elements: {extract}")
print(f"Reversed extracted elements: {reversed_list}")

# Example RUN
Original list: [1,2,3,4,5,6,7,8,9,10]
Extracted first five elements: [1,2,3,4,5]
Reversed extracted elements: [5,4,3,2,1]
