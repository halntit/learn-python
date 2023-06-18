### if __name__ == "__main__" ###
# This is a special variable in Python. 
#   It gets its value depending on how we execute the containing script.
# If we execute the script from the command line using python main.py, 
#   then __name__ will be equal to __main__.
# If we execute the script by importing it from another script, 
#   then __name__ will be equal to the name of the script.

# 1. Module can be run as a standalone program
# 2. Module can be imported and used by other modules

def hello():
    print("Hello World!")

if __name__ == "__main__":
    print("Executing as standalone program/ direct execution")
else:
    print("Executing as imported module")
