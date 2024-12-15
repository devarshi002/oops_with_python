# Write a program that will reverse a four digit number.Also it checks whether the reverse is true.

def reverse_and_check(num):
    reversed_num = int(str(num)[::-1])

    if num == reversed_num:
        return reversed_num, True
    else:
        return reversed_num, False
    
number = int(input("Enter four digit number you want to reverse: "))

if 1000 <= number <= 9999:
  
  reversed_number, is_palindrome = reverse_and_check(number)

  print(f"reversed number: {reversed_number}")
  if is_palindrome:
      print(f"The number is a palindrome.")
  else:
      print("The number is not palindrome.")
else:
    print("plese enter valid four-digit number.")
      


  