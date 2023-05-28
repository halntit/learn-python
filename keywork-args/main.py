### keyword arguments: arguments preceded by an identifier when we pass them to a function

def hello(name, surname):
    print("Hello", name, surname)
hello(surname="Smith", name="Bob")
hello("Bob", surname="Smith")