# User will input (2numbers).Write a program to swap the numbers

def swap_numbers(a,b):
    a, b = b, a
    return a, b

num1 = int(input("Enter a number:"))
num2 = int(input("Enter a number:"))

num1, num2 = swap_numbers(num1, num2)

print(num1, num2)