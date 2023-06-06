### walrus operation :=

happy = True
print(happy)

print(lovePython := True)
print(lovePython := False)

foods = list()

# while True:
#     food = input("What is your favorite food? ")
#     if food == "quit":
#         break
#     foods.append(food)
# print(foods)

while (food := input("What food do you like? ")) != "q":
    foods.append(food)
print(foods)