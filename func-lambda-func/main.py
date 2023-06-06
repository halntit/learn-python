### lambda function: written in one line using lambda keyword

def double(x):
    return x * 2
print(double(5))

dou = lambda x: x * 2
print(dou(5))

multiply = lambda x, y: x * y
print(multiply(2, 3))

full_name = lambda first_name, last_name: f'Full name: {first_name} {last_name}'
print(full_name('John', 'Doe'))

age_check = lambda age: True if age >= 18 else False
print(age_check(20))
print(age_check(15))