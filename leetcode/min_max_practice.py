def max_min(arr):
    if not arr:
        return "Array is empty"
    max_element = arr[0]
    min_element = arr[0]

    for num in arr:
        if num > max_element:
            max_element = num

        if num < min_element:
            min_element = num
    return max_element, min_element

array = [1, 2, 9, 4, 5]
maximum, minimum = max_min(array)
print(f"maximum:{maximum} and minimum: {minimum}")

