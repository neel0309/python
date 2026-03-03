# Dictionary

🧠 How the Program Works
1️⃣ Create a Dictionary
student_marks = {"Alice": 1, "Bob": 2, "Charlie": 3, "Neil": 3}

A dictionary stores key-value pairs

Key → Student name

Value → Marks

Example:

"Alice" → 1

"Bob" → 2

2️⃣ Take User Input
student_name = input("Enter the student's name:")

The user enters a student's name.

The input is stored in the variable student_name.

3️⃣ Check If Student Exists
if student_name in student_marks:

The in operator checks whether the name exists as a key in the dictionary.

If found → display marks.

If not found → display "student not found".

4️⃣ Display Result
print(f"{student_name} marks: {student_marks[student_name]}")

Uses f-strings for formatted output.

Accesses marks using dictionary key lookup.

If not found:

print(f"{student_name} student not found")
▶️ Example Runs
✅ When Student Exists
Enter the student's name: Alice
Alice marks: 1
❌ When Student Does Not Exist
Enter the student's name: David
David student not found
🔑 Concepts Used

Dictionary (key-value pairs)

User input

Conditional statements (if-else)

Membership operator (in)

f-strings

# Slice

🧠 How the Program Works
1️⃣ Create a List Using range()
original_list = list(range(1, 11))

range(1, 11) generates numbers from 1 to 10

list() converts the range into a list

Result:

[1,2,3,4,5,6,7,8,9,10]
2️⃣ Extract the First Five Elements
extract = original_list[:5]

[:5] is list slicing

It selects elements from index 0 to 4

Result:

[1,2,3,4,5]

The original list remains unchanged.

3️⃣ Reverse Using Slicing [::-1]
reversed_list = extract[::-1]

:: → slicing operator

-1 → step backwards

Creates a new reversed list

Does NOT modify extract

Result:

[5,4,3,2,1]
4️⃣ Print the Results
print(f"Original list: {original_list}")
print(f"Extracted first five elements: {extract}")
print(f"Reversed extracted elements: {reversed_list}")
▶️ Example Output
Original list: [1,2,3,4,5,6,7,8,9,10]
Extracted first five elements: [1,2,3,4,5]
Reversed extracted elements: [5,4,3,2,1]
🔑 Concepts Demonstrated

range() function

List conversion using list()

List slicing

Step parameter in slicing

Creating new lists

f-strings