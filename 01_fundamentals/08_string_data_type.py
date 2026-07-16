# String (str): A string is a collection of characters.
# It can contain letters, words, sentences, numbers, symbols, or even be empty.
# Strings are enclosed in single quotes ('') or double quotes ("").

print("String Data Type")
some_str = "Hello World!"
print(f"some_str = {some_str}")
print(f"Type: {type(some_str)}")

print()
print("-" * 50)
print()

print("Empty string")
empty_str = ""
print(f'empty_str = "{empty_str}"')
print(f"Type: {type(empty_str)}")

print()
print("-" * 50)
print()

print("Type Conversion: Almost anything can be converted to a string.\n")

print(f"{1221} : {type(1221)} -> str(1221) = {str(1221)} : {type(str(1221))}")
print(f"{10.5} : {type(10.5)} -> str(10.5) = {str(10.5)} : {type(str(10.5))}")
print(f"{2+3j} : {type(2+3j)} -> str(2+3j) = {str(2+3j)} : {type(str(2+3j))}")
print(f"{True} : {type(True)} -> str(True) = {str(True)} : {type(str(True))}")
print(f"{None} : {type(None)} -> str(None) = {str(None)} : {type(str(None))}")