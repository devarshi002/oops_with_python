class Students:

    def __init__(self, name, marks):
        self.name=name
        self.marks=marks

    def welcome(self):
        print("welcome students", self.name)

    def get_marks(self):
        return self.marks

s1=Students('DEVA', 8.47)
s1.welcome()
print(s1.get_marks())