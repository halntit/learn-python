# type casting
x = 1   # int
y = 2.0 # float
z = "3" # string

print(x + y) # 3.0
print(x + int(z)) # 4
print(str(x) + z) # 13
print(float(x)) # 1.0
print(int(y)) # 2
print(int(float(z))) # 3
print(float(z)) # 3.0
print(str(x)) # 1
print(str(y)) # 2.0
print(str(z)) # 3
