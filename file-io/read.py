try:
    with open('file-io/test.txt') as file:
        print(file.read())
except FileNotFoundError:
    print('File does not exist')
except PermissionError:
    print('You do not have permission to read this file')
except Exception as e:
    print('An unknown error occurred')
    print(e)
else:
    print('File read successfully')
finally:
    print('Done')