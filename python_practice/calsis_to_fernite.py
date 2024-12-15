# Write a program that will convert celsius value to fahrenheit

def celsis_to_fahrenheit(celsis):
    fahrenheit = (celsis *9/5) + 32
    return fahrenheit

celsis = float(input("Enter the temp in celsis: "))


fahrenheit = celsis_to_fahrenheit(celsis)

print(f"temp in C = {celsis} in F = {fahrenheit} ")