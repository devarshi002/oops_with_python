# Define a class Rectangle with attributes length and width. Use a constructor to initialize these attributes when the object is created

class Rectangle:
    def __init__(self, length, width):
        self.length=length
        self.width=width


#create object
rect = Rectangle(5,10)

#Display
print("length:", rect.length)
print("width", rect.width)