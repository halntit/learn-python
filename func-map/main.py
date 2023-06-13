### function map: used with lists and iterables
# map(function, iterable)

store = [
    ('Apple', 10.00),
    ('Banana', 25.50),
    ('Orange', 31.50),
    ('Grape', 40.00),
    ('Mango', 20.50),
    ('Peach', 30.50)
]
print(store)
print("=====================================")

store.sort(key=lambda x: x[1]) # sort by price
print(store)
print("=====================================")

toEuros = map(lambda data: (data[0], data[1] * 0.82), store)
toEuros = list(toEuros) # convert to list
print(toEuros)
print("=====================================")