def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

answer = int(input("Enter a number: "))

fact = factorial(answer)

print(f'Factorial of {answer} is {fact}')



