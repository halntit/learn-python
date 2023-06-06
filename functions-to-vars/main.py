def hello():
    print("Hello, world!")

hello()

print(hello) # address of the function hello in memory in hexadecimal format
hi = hello # like alias
print(hi) # the same address as hello

hi() # the same as hello()

#===============================================================================
say = print
say("Using say instead of print!") # the same as print("Hello, world!")