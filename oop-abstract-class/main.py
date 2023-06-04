### abstract class: abstraction
# ABC: abstract base class
# @abstractmethod: decorator
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass

class Dog(Animal):
    def eat(self):
        print("dog is eating")

class Cat(Animal):
    def eat(self):
        print("cat is eating")

dog = Dog()
cat = Cat()
dog.eat()
cat.eat()

#animal = Animal() # error : cannot instantiate abstract class Animal
# don't allow to create a Animal object