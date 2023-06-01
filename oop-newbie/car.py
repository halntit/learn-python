### OOP: Object-Oriented Programming
### Car class

class Car:
    # attributes
    make = None
    model = None
    year = None
    color = None

    # constructor
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    # methods
    def drive(self):
        print(f"{self.make} {self.model} is driving...")

    def stop(self):
        print(f"{self.make} {self.model} is stopping...")