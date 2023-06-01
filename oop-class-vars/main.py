from car import Car

car1 = Car('Honda', 'Civic', 2020, 'Red')
print(car1.make)

car2 = Car('Honda', 'Accord', 2020, 'Blue')
print(car2.make, car2.model)

car1.drive()
car2.stop()

print(car1.wheels)
print(car2.wheels)

# change class variable
Car.wheels = 2
print(car1.wheels)
print(car2.wheels)