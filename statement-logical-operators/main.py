### logical operators

temp = int(input("What is the temperature outside?: "))
if temp >= 0 and temp <= 30:
    print("The temperature is good today")
    print("Go outside and enjoy it!")
#elif temp < 0 or temp > 30:
elif not(temp < 0 or temp > 30):
    print("The temperature is bad today")
    print("Stay inside and play video games")
else:
    print("The temperature is not good today")
    print("Stay inside and play video games")

# and
print(True and True)

# or
print(True or False)

# not
print(not(True))