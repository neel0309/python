# Even or Odd Number Checker

# Description
This Python script checks whether a given number is even or odd.
It prompts the user to enter a number and then determines if the number is divisible by 2.

# How It Works
The user inputs a number.
The program uses the modulus operator %.
If number % 2 == 0, the number is even.
Otherwise, it is odd.

# code
number = int(input("Enter a number: "))
if number % 2 == 0:
print(f"{number} is an even number")
else:
print(f"{number} is an odd number")

# output

Enter a number: 10
10 is an even number
Enter a number: 7
7 is an odd number


# Sum of Numbers from 1 to 50
# Description

This Python script calculates the sum of numbers from 1 to 50 using a for loop.

It iterates through numbers 1 to 50 (inclusive), adds them together, and prints the final result.

# How It Works

Initialize a variable sum1 to 0

Use range(1, 51) to generate numbers from 1 to 50

Add each number to sum1

Print the final sum after the loop ends

# Code
sum1 = 0

for i in range(1, 51):
sum1 += i

print(f"The sum of numbers from 1 to 50 is {sum1}")
# Output
The sum of numbers from 1 to 50 is 1275