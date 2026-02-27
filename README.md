# Factorial

This Python script calculates the factorial of a number entered by the user using a recursive function.

A factorial of a number n (written as n!) means:

n! = n × (n-1) × (n-2) × ... × 1

Example:

5! = 5 × 4 × 3 × 2 × 1 = 120

By definition:

0! = 1

# How the code works ?

The function factorial(n) calculates the factorial of n.

It uses recursion, meaning the function calls itself.

Base case:
When n == 0, the function returns 1.
This stops the recursion.

Recursive case:
The function returns n * factorial(n-1)
This continues reducing the number until it reaches 0.

# Math Operations Program

This Python script:

Takes a number as input from the user

Calculates:

        Square root

        Natural logarithm

        Radians conversion

Prints the results

It uses Python’s built-in math module.

# Import the Math Module
    import math

Imports Python’s built-in math library.

Gives access to mathematical functions like:

    sqrt()
    
    log()
    
    radians()

# Take User Input
    answer = int(input("Enter a number: "))

Prompts the user to enter a number.

input() returns a string.

int() converts it into an integer.

The value is stored in the variable answer.

Example:

Enter a number: 25

# Calculate and Print Results
    Square Root
    print(f'Square root {math.sqrt(answer)}')

    math.sqrt(answer) returns the square root.

Example:

Square root 5.0

(since √25 = 5)

# Logarithm
    print(f'Logarithm {math.log(answer)}')

    math.log(answer) returns the natural logarithm (base e).

Example:

Logarithm 3.2188758248682006

(ln(25))

If you wanted base 10 instead, you would use:

math.log10(answer)
# Radians Conversion
    print(f'Sine {math.sin(answer)}')
    math.sin(math.radians(answer))