def greet(name):
    return f"Hello , {name}"


def call_function(func, name):
    return func(name)


result = call_function(greet, "Deva")
print(result)