def modify_mutable(lst):
    print(f"function before modification: {lst}")
    lst.append(4)
    print(f"fuction after modification: {lst}")

my_list =[1,2,3]
print(f"before function call: {my_list}")

modify_mutable(my_list)
print(f"after function call: {my_list}")