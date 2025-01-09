class Students:
    college_name = "pandav college"

    def __init__(self, name, marks):
        self.name=name
        self.marks=marks
    

s1 = Students("Devarshi", 8.47)
print(s1.name, s1.marks)
print(s1.college_name)