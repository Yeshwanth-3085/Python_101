# float: Basically fractional numbers and decimal numbers
# again negative end to positive end
# also precision isn't always great

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
print(small)
print(large)
print(type(small), type(large))

print()
print("-" * 50)
print()


# Floating point numbers are stored in binary,
# so some decimal values cannot be represented exactly.
print("Floating Point Precision")

print(0.1 + 0.2)
print(0.1 + 0.2 == 0.3)

print()
print("-" * 50)
print()

print("Type Conversion")

print(float(10))
print(float("3.14"))
print(int(3.99))

print(type(float(10)))

print()
print("-" * 50)
print()

positive_inf = float("inf")
negative_inf = float("-inf")
not_a_number = float("nan")

print(positive_inf)
print(negative_inf)
print(not_a_number)