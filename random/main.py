### rand: random number generator

import random

x = random.randint(1, 6) # 1 <= x <= 6 (inclusive)
print(x)

y = random.random() # 0 <= y < 1
print(y)

z = random.uniform(1, 6) # 1 <= z < 6
print(z)

myList = ['rock', 'paper', 'scissors']
w = random.choice(myList)
print(w)

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
print(cards)
random.shuffle(cards)
print(cards)