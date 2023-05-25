import time

### for loop
for i in range(1, 11):
    print(i)

# for loop with step
for i in range(1, 11, 2):
    print(i)

for i in "hello world":
    print(i)

# for seconds in range(10, 0, -1):
#     print(seconds)
#     time.sleep(1)
# print("Happy New Year!")

# for loop with else
for i in range(1, 11):
    print(i)
else:
    print("Loop finished")

# nested for loop
for i in range(1, 11):
    for j in range(1, 11):
        print(i, j)

rows = int(input("How many rows? "))
columns = int(input("How many columns? "))
symbol = input("Enter a symbol to use: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()
