def modify_immutable(x):
    print(f"inside function before modification: {x}")
    x = x +1
    print(f"inside function after modification: {x}")

num = 10
print(f"before function call: {num}")
modify_immutable(num)
print(f"after function call: {num}")


# Explanation: The original num is not changed because integers are immutable. The modification creates a new object.

