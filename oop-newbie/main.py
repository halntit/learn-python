from car import Car

car1 = Car('Honda', 'Civic', 2020, 'Red')
print(car1.make)

car2 = Car('Honda', 'Accord', 2020, 'Blue')
print(car2.make, car2.model)

car1.drive()
car2.stop()