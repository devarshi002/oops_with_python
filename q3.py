# Create a class Circle with an attribute radius and a member function calculate_area() that calculates and returns the area of the circle. Create an object and call the member function.

class Circle:
    def __init__(self, radius):
        self.radius=radius

    #member function to calculate the area of the circle
    def calculate_area(self):
        return 3.14 * self.radius * self.radius
    

#create an object
circle = Circle(5.0)

#display

print("Area of Circle:", circle.calculate_area())