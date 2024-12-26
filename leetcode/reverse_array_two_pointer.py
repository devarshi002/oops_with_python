#using two pointer approach

def reverse_array(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left +=1
        right -=1

    return arr


array=[1,2,3,4,5,6]
reversed_array=reverse_array(array)
print(reversed_array)