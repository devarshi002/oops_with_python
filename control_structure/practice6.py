number = int(input("enter a positive number: "))

factorial = 1
i=1


while i <=number:
    factorial *=i
    i+=1

print(f"the factorial of {number} is : {factorial}")