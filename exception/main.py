### exception: events that interrupt the normal flow of execution

try:
    numrator = int(input("Enter a number: "))
    denominator = int(input("Enter a number: "))
    result = numrator / denominator

except ZeroDivisionError as e:
    print(e)
    print("You can't divide by zero!")
except ValueError as e:
    print(e)
    print("You must enter a number!")
except Exception as e:
    print(e)
    print("Something went wrong!")

else:
    print("No exceptions were thrown!")
    print(result)

finally:
    print("This will always execute!")
