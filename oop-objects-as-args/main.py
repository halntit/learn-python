### objects as arguments: passing objects as arguments to functions

class Car:
    color = None

class Motorcycle:
    color = None

def change_color(vehicle, color):
    vehicle.color = color

car1 = Car()
print(car1.color)
change_color(car1, 'red')
print(car1.color)
car2 = Car()
print(car2.color)
change_color(car2, 'blue')
print(car2.color)

motorcycle1 = Motorcycle()
print(motorcycle1.color)
change_color(motorcycle1, 'black')
print(motorcycle1.color)