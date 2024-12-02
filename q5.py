class Car:
    #class veriable to count the number of cars
    numbers_of_cars = 0

    def __init__(self, make, model, year):
        self.make=make
        self.model=model
        self.year=year

        #Increment the number of cars whenever a new car is created
        Car.numbers_of_cars += 1

    def display_info(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}")

#Create car objects

car1 = Car("Toyota", "Corolla",2020)
car2 = Car("Honda","Civic",2018)

#display
car1.display_info()
car2.display_info()

#display total number of cars

print("total numbers of cars:",Car.numbers_of_cars)