# Easy Level
# Find Two Numbers with a Given Sum

# Problem: Find two numbers in a sorted array that add up to a target sum.
# Input: arr = [1, 2, 3, 4, 6], target = 6
# Output: [1, 3] (since arr[1] + arr[3] = 6)


# Initialize Two Pointers:

# Set one pointer (left) at the beginning of the array (index 0).
# Set the other pointer (right) at the end of the array (last index).
# Check the Sum:

# Calculate the sum of the elements at left and right.
# If the sum equals the target, return the indices or the numbers.
# If the sum is less than the target, move the left pointer one step forward.
# If the sum is greater than the target, move the right pointer one step backward.
# Repeat:

# Continue until the two pointers meet or the solution is found.


def two_num(arr, target):
    left=0
    right=len(arr) - 1
    
    while left < right:
        sum_of_ele = arr[left] + arr[right]

        if sum_of_ele == target:
            return [left, right]
        elif sum_of_ele < target:
            left +=1
        else:
            right -=1
    return "No such pair exists"

arr=[1,2,3,4,6]
target=6
result=two_num(arr, target)

print("Indices:", result)
print("Numbers:",[arr[i] for i in result])