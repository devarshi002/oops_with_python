def rebind_mutable(lst):
    print(f"function before rebind: {lst}")
    lst=[10,20,30]
    print(f"function after rebind: {lst}")

my_list = [1,2,3]
print(f"before function call: {my_list}")
rebind_mutable(my_list)
print(f"after function call: {my_list}")