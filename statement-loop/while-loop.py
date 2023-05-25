### while loop

command = ''

while command != "exit": 
    if len(command) > 0:
        print("You typed " + command)
    command = input("Type a command or 'exit' to exit application: ")