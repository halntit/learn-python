### dictionary comprehension: used with dictionaries and returns a new dictionary with less syntax.

cities_in_F = {"New York": 40, "Los Angeles": 30, "Chicago": 20, "Houston": 10}
print(cities_in_F)
print("=====================================")

cities_in_C = {city: temperature * 9/5 + 32 for city, temperature in cities_in_F.items()}
print(cities_in_C)
print("=====================================")