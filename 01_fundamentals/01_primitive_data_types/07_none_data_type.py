# None represents the absence of a value.
# It is not the same as 0, False, or an empty string.

x = None

print("None Data Type")
print(f"x = {x}")
print(type(x))

print()
print("-" * 50)
print()

print("Comparison")
print(f"None == None : {None == None}")
print(f"None is None : {None is None}")
print(f"None == False : {None == False}")
print(f"None == 0 : {None == 0}")
print(f"None == '' : {None == ''}")

print()
print("-" * 50)
print()

# Use 'is None' instead of '== None'
# It is the recommended Python style.

print("Checking for None")
x = None
print(f"x is None : {x is None}")
print(f"x == None : {x == None}")

print()
print("-" * 50)
print()

# None is often used as a placeholder
# until a real value is assigned.

print("Truthiness")
print(f"bool(None) : {bool(None)}")

print()
print("-" * 50)
print()

print("Common Use Case")
num = None
print(f"None: num = {num}")
num = 69
print(f"69: num = {num}")