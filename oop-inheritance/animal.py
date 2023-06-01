### class Animal

class Animal:

    #attributes
    alive = True
    name = ""

    def __init__(self):
        pass

    def eat(self, food):
        print(f"This {self.name} is eating {food}")

    def sleep(self):
        print("This {} is sleeping".format(self.name))

class Rabbit(Animal):
    name = "Rabbit"

    def run(self):
        print("This {} is running".format(self.name))

class Fish(Animal):
    name = "Fish"
    def swim(self):
        print("This {} is swimming".format(self.name))

class Dog(Animal):
    name = "Dog"
    def bark(self):
        print("This {} is barking".format(self.name))