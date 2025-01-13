try:
    num = int(input("Enter a number: "))
    print(f"the number is {num}")
except ValueError:
    print("Invalid input! please enter a valid integer")