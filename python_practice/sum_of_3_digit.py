# Write a program that will give you the sum of 3 digits

def sum_of_digits(a,b,c):
    return a + b + c

digit1 = int(input("Enter the first digit: "))
digit2 = int(input("Enter the second digit: "))
digit3 = int(input("Enter the third digit: "))

result = sum_of_digits(digit1, digit2, digit3)
print(f"The sum of {digit1}, {digit2}, {digit3} is: {result}")