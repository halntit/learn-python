### super function: calling parent class methods and properties

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

class Square(Rectangle):
    def __init__(self, length, width):
        super().__init__(length, width)

    def area(self):
        return self.length * self.width

class Cube(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height

    def volume(self):
        return self.length * self.width * self.height

r = Rectangle(10, 20)
s = Square(10, 20)
c = Cube(10, 20, 30)

print(s.area())
print(c.volume())


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(self.name, self.age)

class Student(Person):
    def __init__(self, name, age, major):
        super().__init__(name, age)
        self.major = major

    def show(self):
        super().show()
        print(self.major)

p = Person("John", 36)
s = Student("Mike", 20, "Computer Science")
s.show()
p.show()