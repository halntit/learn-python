
filePath = 'file-io/test.txt'

writeMode = 'w'
appendMode = 'a'

with open(filePath, writeMode) as file:
    file.write('Hello, world!')
    file.write('\n')
    file.write('This is a test file')
    file.write('\n')
    file.write('This is the last line')

with open(filePath) as file:
    print(file.read())

print('==========')

with open(filePath, appendMode) as file:
    file.write('\n')
    file.write('Hello, counter-world!')

with open(filePath) as file:
    print(file.read())