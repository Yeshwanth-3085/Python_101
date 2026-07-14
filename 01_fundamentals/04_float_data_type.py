# float: Basically fractional numbers and decimal numbers
# again negative end to positive end

a = -10.5
b = 0.0
c = 10.5

print("Flaot Data Type")
print(a, b, c)
print(type(a), type(b), type(c))
print()
print("-" * 50)
print()

small = 3.2e-4
large = 5.7e8

print("Scientific Notation")
print(f"3.2e-4: {small}")
print(f"5.7e8: {large}")
print(type(small), type(large))

print()
print("-" * 50)
print()


# Floating point numbers are stored in binary,
# so some decimal values cannot be represented exactly.
print("Floating Point Precision")

print(f"Supposed to be: 0.1 + 0.2 = 0.3")
print(f"Reality: 0.1 + 0.2 = {0.1 + 0.2}")
print(f"0.1 + 0.2 == 0.3: {0.1 + 0.2 == 0.3}")

print()
print("-" * 50)
print()

print("Type Conversion")

print(f"int -> float: 10 -> {float(10)}")
print(f"str -> float: '3.14' -> {float('3.14')}")
print(f"float -> int: 3.99 -> {int(3.99)}")

print()
print("-" * 50)
print()

import math

x = float('nan')
y = float('inf')
z = float('-inf')

print("Special float cousins")

print()

print(f'{x}: {type(x)}, {y}: {type(y)}, {z}: {type(z)}')

print()

print(f'nan == nan: {x == x}')
print(f'inf == inf: {y == y}')
print(f'-inf == -inf: {z == z}')

print()

print(f'inf + 1 = {y + 1}')
print(f'inf * -1 = {y * -1}')
print(f'inf - inf = {y - y}')
print(f'inf / inf = {y / y}')
print(f'0.0 * inf = {0.0 * y}')

print()

print(f'math.isnan(nan): {math.isnan(x)}')
print(f'math.isinf(inf): {math.isinf(y)}')
print(f'math.isinf(-inf): {math.isinf(z)}')
print(f'math.isfinite(3.14): {math.isfinite(3.14)}')