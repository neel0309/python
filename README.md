
# TASK 1

🔹 Step 1: Taking Input
first_number = input("Enter the first number: ")


input() shows the message:
Enter the first number:

The user types something.

⚠️ Important: input() always returns a string, not a number.

That string is stored in first_number.

Example:
If user types 10
Then:

first_number = "10"   # string

second_number = input("Enter the second number: ")


Same process:
If user types 5

second_number = "5"   # string

🔹 Step 2: Why We Use int()

Because input values are strings:

"10" + "5"  # gives "105"


That would concatenate, not add.

So we convert them to integers:

int(first_number)
int(second_number)


Now they become real numbers:

10
5

🔹 Step 3: Addition
print("Addition:" , int(first_number) + int(second_number))


What happens:

Convert both strings to integers.

Add them.

Print result.

Example output:

Addition: 15

🔹 Step 4: Subtraction
print("Substraction:" , int(first_number) - int(second_number))


10 - 5 = 5

Output:

Substraction: 5

🔹 Step 5: Multiplication
print("Multiplication:" , int(first_number) * int(second_number))


10 × 5 = 50

Output:

Multiplication: 50

🔹 Step 6: Division
print("Division:" , int(first_number) / int(second_number))


10 ÷ 5 = 2.0

⚠️ Notice:
Division / always returns a float in Python.

Even:

10 / 5  # 2.0

# ============

# Task 2

Ask for the first name

first_name = input("Enter your first name: ")


The input() function displays the message "Enter your first name: ".

The user types their first name.

The entered value is stored in the variable first_name.

Ask for the second name

second_name = input("Enter your second name: ")


The program displays "Enter your second name: ".

The user types their second name.

The entered value is stored in the variable second_name.

Combine the names

full_name = first_name + " " + second_name


The program joins first_name and second_name.

" " adds a space between them.

The combined result is stored in the variable full_name.

Display the greeting message

print(f"Hello, {full_name}! Welcome to the python program.")


The print() function displays output on the screen.

The f before the string makes it an f-string, allowing variable values inside {}.

{full_name} is replaced with the user's full name.

The final message appears, for example:

Hello, John Smith! Welcome to the python program.