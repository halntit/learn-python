### method chaining

class Car:

    def turn_on(self):
        print("You start the engine")
        # if no return, it will return None
        return self

    def drive(self):
        print("You drive the car")
        return self

    def brake(self):
        print("You brake the car")
        return self

    def turn_off(self):
        print("You stop the engine")
        return self

aCar = Car()
aCar.turn_on().drive().brake().turn_off()