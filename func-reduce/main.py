### reduce: used with iterables and returns a single value.

import functools

letters = ["H", "e", "l", "l", "o"]
print(letters)
print("=====================================")

reduced = functools.reduce(lambda x, y: x + y, letters)
# steps
# 1. take first 2 elements (H, e)
# 2. take next 2 elements (He, l)
# 3. take next 2 elements (Hel, l)
# 4. take next 2 elements (Hell, o)
# 5. return final value
print(reduced)
print("=====================================")

factorial = [1, 2, 3, 4, 5]
print(factorial)
print("=====================================")
print(functools.reduce(lambda x, y: x * y, factorial))
print("=====================================")