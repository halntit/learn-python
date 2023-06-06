### higher order function: a function that takes a function as an argument or returns a function as a result

def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def hello(func):
    text = func("Hello, world!")
    print(text)

hello(loud)
hello(quiet)

#===============================================================================
def divisor(x): # is higher order function
    def dividend(y): # is closure
        return y / x
    return dividend

devide_by_2 = divisor(2)
print(devide_by_2(10))
# steps
# 1. divisor(2) is called and returns dividend(y)
# 2. dividend(y) is called and returns y / x
# 3. devide_by_2(10) is called and returns 10 / 2
