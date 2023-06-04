### method overriding: overriding method of parent class to override method of child class 

class Animal:
    def eat(self):
        print("This animal is eating")

class Dog(Animal):
    def eat(self):
        print("This dog is eating")

class Cat(Animal):
    pass

dog = Dog()
dog.eat()
cat = Cat()
cat.eat()