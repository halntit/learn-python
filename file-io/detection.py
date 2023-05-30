import os

# Read file
def read_file(path):
    if os.path.exists(path):
        print('File exists')
        if os.path.isfile(path):
            print('File is a file')
            with open(path, 'r') as f:
                print(f.read())
        elif os.path.isdir(path):
            print('File is a directory')
            print(os.listdir(path))
        else:
            print('File is not a file or directory')
    else:
        print('File does not exist')

path = 'file-io/test.txt'
read_file(path)

print('==========')

path = 'file-io'
read_file(path)

print('==========')

path = 'file-io/does-not-exist.txt'
read_file(path)