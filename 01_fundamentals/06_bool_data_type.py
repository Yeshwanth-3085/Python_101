# Boolean represents logical values:
# True or False.
# In Python, True behaves like 1 and False behaves like 0 in arithmetic.

a = True
b = False

print("Boolean Data Type")
print(f"a = {a}, b = {b}")
print(type(a), type(b))

print()
print("-" * 50)
print()

# Comparison operators produce boolean values (True or False)
print("Comparison Operators produce boolean values (True or False)")
print(f"10 > 5 : {10 > 5}")
print(f"10 < 5 : {10 < 5}")
print(f"10 == 10 : {10 == 10}")
print(f"10 != 10 : {10 != 10}")
print(f"10 >= 5 : {10 >= 5}")
print(f"10 <= 5 : {10 <= 5}")

print()
print("-" * 50)
print()

# Almost any value is evaluated to True if it has some sort of content.
# Any string is True, except empty strings.
# Any number is True, except 0.
# Any list, tuple, set, and dictionary are True, except empty ones.

print("Truthiness (Type Conversion): Anything with a value becomes True unless it's zero or empty.")
print(f"bool(1) : {bool(1)}")
print(f"bool(0) : {bool(0)}")
print(f"bool(-10) : {bool(-10)}")
print(f"bool(3.14) : {bool(3.14)}")
print(f"bool(0.0) : {bool(0.0)}")
print(f"bool('Hello') : {bool('Hello')}")
print(f"bool('') : {bool('')}")
print(f"bool([1, 2]) : {bool([1, 2])}")
print(f"bool([]) : {bool([])}")
print(f"bool(None) : {bool(None)}")

print()
print("-" * 50)
print()

print("Boolean Operators")
print(f"True and True : {True and True}")
print(f"True and False : {True and False}")
print(f"True or False : {True or False}")
print(f"not True : {not True}")
print(f"not False : {not False}")

print()
print("-" * 50)
print()

# bool is a subclass of int
# True behaves like 1
# False behaves like 0

print("Interesting Fact: bool is lowkey int, True is 1, False is 0")
print(f"True + True : {True + True}")
print(f"True + False : {True + False}")
print(f"False + False : {False + False}")
print(f"True * 10 : {True * 10}")
print(f"int(True) : {int(True)}")
print(f"int(False) : {int(False)}")