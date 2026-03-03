# Dictionary

1️⃣ Dictionary Creation
dict = {"Alice": 1, "Bob": 2, "Charlie": 3, "Neil": 3}

A dictionary is created where:

Key → Student name

Value → Marks

Example:

"Alice" → 1

"Bob" → 2

2️⃣ User Input
take = input("Enter the student's name:")

The program asks the user to enter a student's name.

The input is stored in the variable take.

3️⃣ Searching the Dictionary
for name in dict:
    if name == take:
        print(f"{name} marks: {dict[name]}")

The program loops through each name in the dictionary.

If the entered name matches a key:

It prints the student's marks.

▶️ Example Run
Enter the student's name: Alice
Alice marks: 1

# Slice

1️⃣ Create the Original List
original_list = [1,2,3,4,5,6,7,8,9,10]

A list of numbers from 1 to 10 is created.

This list remains unchanged throughout the program.

2️⃣ Extract First Five Elements
extract = original_list[:5]

[:5] is list slicing.

It creates a new list containing the first five elements.

The original list is not modified.

After slicing:

extract = [1, 2, 3, 4, 5]
3️⃣ Print the Lists
print(f"original list: {original_list}")
print(f"Extracted first five elements:{extract}")

Displays:

The original full list

The sliced list

4️⃣ Reverse the Extracted List
extract.reverse()

reverse() modifies the list in place

It does not create a new list

It does not return anything (None)

After reversing:

extract = [5, 4, 3, 2, 1]
5️⃣ Print the Reversed List
print(f"Reversed extracted elements: {extract}")
▶️ Example Output
original list: [1,2,3,4,5,6,7,8,9,10]
Extracted first five elements: [1,2,3,4,5]
Reversed extracted elements: [5,4,3,2,1]