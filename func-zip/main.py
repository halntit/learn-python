### function zip: zip(*iterables): used to combine 2 or more iterables and returns a tuple for each iteration.
# Syntax: zip(iterable1, iterable2, iterable3, ...)

usernames = ['Sunny', 'Bunny', 'Chinny', 'Vinny', 'Pinny']
passwords = ('sun', 'bun', 'chin', 'vin', 'pin')

print(usernames)
print(passwords)
print("=====================================")

users = zip(usernames, passwords)
print(type(users))
print(list(users))
print("=====================================")

login_date = ['1/1/2021', '2/1/2021', '3/1/2021', '4/1/2021', '5/1/2021']
last_login_date = ['1/1/2021', '2/1/2021', '3/1/2021', '4/1/2021', '5/1/2021']
login_status = [True, False, True, False, True]

users = zip(usernames, passwords, login_date, last_login_date, login_status)
print(list(users))
print("=====================================")
