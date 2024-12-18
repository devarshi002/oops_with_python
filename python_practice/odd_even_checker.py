import time

def check_even_odd():
    print("Welcome to the Odd-Even Checker!")
    time.sleep(1)  # Adding a short pause for dramatic effect

    # Get user input
    number = int(input("Enter a number: "))
    print("Processing...")
    time.sleep(2)  # Simulating "processing" time

    # Check if the number is even or odd
    if number % 2 == 0:
        print(f"🎉 The number {number} is Even! 🎉")
    else:
        print(f"🎉 The number {number} is Odd! 🎉")
    
    print("Thanks for using the Odd-Even Checker! 😄")

# Run the function
check_even_odd()
