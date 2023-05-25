### loop control

# break
for i in range(1, 11):
    if i == 5:
        break
    print(i)

# continue
for i in range(1, 11):
    if i == 5:
        continue
    print(i)

# pass: used when a statement is required syntactically but you do not want any command or code to execute
for i in range(1, 11):
    if i == 5:
        pass
    print(i)

for i in range(1, 11):
    if i == 5:
        pass
    else:
        print(i)
