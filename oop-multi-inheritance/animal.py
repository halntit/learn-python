### multi-inheritance: a class that derives from multiple classes

### class Predator
class Predator:
    def hunt(self):
        print("This animal is hunting")

### class Prey
class Prey:
    def flee(self):
        print("This animal is fleeing")

class Rabbit(Prey):
    pass

class Dog(Predator):
    pass

class Fish(Prey, Predator):
    pass