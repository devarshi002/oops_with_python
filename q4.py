# Create a class Person with attributes name and age. Implement a default constructor that assigns default values to the attributes. Create an object and display the values.

class Person:
    def __init__(self):
        self.name = "deva"
        self.age = 22

#create object

babubhaiya = Person()

print("Name:", babubhaiya.name)
print("age:",babubhaiya.age)