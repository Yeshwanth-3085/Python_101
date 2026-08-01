# String Methods: Search and Replace Methods

some_str = "Hello World!"

print("\nfind(): Searches the string for a specified substring and returns the position of where it was found.")
print("Returns -1 if not found.")
print(f"some_str = {some_str}")
print(f'some_str.find("Wor") -> {some_str.find("Wor")}')
print(f'some_str.find("o") -> {some_str.find("o")}')
print(f'some_str.find("P") -> {some_str.find("P")}')

print()
print("-" * 50)
print()

print("rfind(): Searches the string from the end and returns the last position where the substring was found.")
print("Returns -1 if not found.")
print(f"some_str = {some_str}")
print(f'some_str.rfind("Wor") -> {some_str.rfind("Wor")}')
print(f'some_str.rfind("o") -> {some_str.rfind("o")}')
print(f'some_str.rfind("P") -> {some_str.rfind("P")}')

print()
print("-" * 50)
print()

print("index(): Searches the string for a specified substring and returns the position of where it was found.")
print("Raises ValueError if not found.")
print(f"some_str = {some_str}")
print(f'some_str.index("Wor") -> {some_str.index("Wor")}')
print(f'some_str.index("o") -> {some_str.index("o")}')
# print(f'some_str.index("P") -> {some_str.index("P")}')

print()
print("-" * 50)
print()

print("rindex(): Searches the string from the end and returns the last position where the substring was found.")
print("Raises ValueError if not found.")
print(f"some_str = {some_str}")
print(f'some_str.rindex("Wor") -> {some_str.rindex("Wor")}')
print(f'some_str.rindex("o") -> {some_str.rindex("o")}')
# print(f'some_str.rindex("P") -> {some_str.rindex("P")}')

print()
print("-" * 50)
print()

print("count(): Returns the number of times a specified substring occurs in a string.")
print(f"some_str = {some_str}")
print(f'some_str.count("ll") -> {some_str.count("ll")}')
print(f'some_str.count("o") -> {some_str.count("o")}')
print(f'some_str.count("P") -> {some_str.count("P")}')

print()
print("-" * 50)
print()

print("startswith(): Returns True if the string starts with the specified prefix.")
print(f"some_str = {some_str}")
print(f'some_str.startswith("H") -> {some_str.startswith("H")}')
print(f'some_str.startswith("Hello") -> {some_str.startswith("Hello")}')
print(f'some_str.startswith("W") -> {some_str.startswith("W")}')

print()
print("-" * 50)
print()

print("endswith(): Returns True if the string ends with the specified suffix.")
print(f"some_str = {some_str}")
print(f'some_str.endswith("!") -> {some_str.endswith("!")}')
print(f'some_str.endswith("World!") -> {some_str.endswith("World!")}')
print(f'some_str.endswith("H") -> {some_str.endswith("H")}')

print()
print("-" * 50)
print()

print("replace(): Replaces all occurrences of a specified substring with another substring.")
print(f"some_str = {some_str}")
print(f'some_str.replace("World", "Python") -> {some_str.replace("World", "Python")}')
print(f'"banana".replace("a", "o") -> {"banana".replace("a", "o")}')

print()