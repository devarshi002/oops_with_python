try:
    num = int(input("Enter a number: "))
    result = 10/num
    print(f"Result: {result}")
except ValueError:
    print("Invalid input! please enter a valid int")
except ZeroDivisionError:
    print("Cannot divide by zero")