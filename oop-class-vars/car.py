### OOP: Object-Oriented Programming
### Car class

class Car:

    # attributes
    wheels = 4 # class variable

    # constructor
    def __init__(self, make, model, year, color):
        self.make = make      # instance variable
        self.model = model    # instance variable
        self.year = year      # instance variable
        self.color = color    # instance variable

    # methods
    def drive(self):
        print(f"{self.make} {self.model} is driving...")

    def stop(self):
        print(f"{self.make} {self.model} is stopping...")