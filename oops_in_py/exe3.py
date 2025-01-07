class Student:

    #default constructor
    def __init__(self):
        print("hello")

    #parameterized constructor
    def __init__(self, fullname, marks):
        self.name = fullname
        self.marks = marks
        
s1 = Student("Deva", 93)
print(s1.name, s1.marks)

s2 = Student("Krishna", 90)
print(s2.name, s2.marks)