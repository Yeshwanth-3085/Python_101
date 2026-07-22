# String Formatting

print("f-strings insert expressions or variable values into a string using curly brace {} placeholders.")
some_str = "Hello World!"
print("some_str = Hello World!")
print('f"some_str = {some_str}" -> ' + f"some_str = {some_str}")
print('f"5 + 3 = {5 + 3}" -> ' + f"5 + 3 = {5 + 3}")

print()
print("-" * 50)
print()

# str.format()
print("str.format() inserts values into a template string using {} placeholders.")
print("\nEmpty {} Placeholders (Positional)")
print('"{} owns a {}.".format("Alice", "cat")')
print("{} owns a {}.".format("Alice", "cat"))

print("\nIndexed Placeholders")
print('"{1} owns a {0}.".format("Alice", "cat")')
print("{1} owns a {0}.".format("Alice", "cat"))

print("\nKeyword / Named Placeholders")
print('"{name} owns a {pet}.".format(pet = "cat", name = "Alice")')
print("{name} owns a {pet}.".format(pet = "cat", name = "Alice"))

print()
print("-" * 50)
print()

# %-formatting (legacy)
print("%-formatting (legacy), generally replaced by f-strings")
print('"%s brought %d apples for $%f" % ("Alice", 5, 4.67)')
print("%s brought %d apples for $%f" % ("Alice", 5, 4.67))

print()
print("-" * 50)
print()

# Format Specifiers
print("Format Specifiers (The Mini Language)")
print("The format specification mini-language is a big rabbit hole. If you want to explore it further, the official documentation covers many more options. Here are a few common examples:")

print("\nPrecision (:.Nf)")
print('"Price: {:.2f}".format(19.995)')
print("Price: {:.2f}".format(19.995))

print("\nComma Separators (:,)")
print('"Number: {:,}".format(1000000)')
print("Number: {:,}".format(1000000))

print()
print("-" * 50)
print()

# Escaping Literal Braces
# Curly braces {} are placeholders in formatted strings.
# Double braces {{ }} print literal braces.
print("Escaping Literal Braces: Double braces are used to print literal braces. Single braces are reserved for placeholders.")
print()
print('f"{{}}" -> ' + f"{{}}")
print('f"{{121}}" -> ' + f"{{121}}")
print()
print('"{{}}".format() -> ' + "{{}}".format())
print('"{{121}}".format() -> ' + "{{121}}".format())