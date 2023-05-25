### if statement

age = int(input("How old are you?: "))

if age < 18:
    print("You are not allowed to drink alcohol")
elif age == 18:
    print("You are allowed to drink alcohol")
else:
    print("You are allowed to drink alcohol and you can drive")