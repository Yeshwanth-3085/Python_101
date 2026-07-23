# Escape Characters in Strings

# Quote Escape Characters: (\'), (\")
print("\nQuote Escape Characters\n")

print("(\\'): " + "'\\'Hello\\'' -> " + '\'Hello\'')

print()

print('(\\"): ' + '"\\"Hello\\"" -> ' + "\"Hello\"")

print()
print("-" * 50)
print()

# Common Escape Characters: (\n), (\t), (\\)
print("Common Escape Characters\n")

print("(\\n): " + "\"Hello\\nWorld!\" -> " + "Hello\nWorld!")

print()

print("(\\t): " + "\"Hello\\tWorld!\" -> " + "Hello\tWorld!")

print()

print(r"(\\): " + r"\"Hello\\World!\" -> " + "Hello\\World!")

print()
print("-" * 50)
print()

# Control Escape Characters: (\b), (\r), (\v)
print("Control Escape Characters\n")

print("(\\b): " + "\"Hello\\bWorld!\" -> " + "Hello\bWorld!")

print()

print("(\\r): " + "\"Hello\\rWorld!\" ↓ ")
print("Hello\rWorld!")

print()

print("(\\v): " + "\"Hello\\vWorld!\" -> " + "Hello\vWorld!")

print()
print("-" * 50)
print()

# Raw Strings (r"...")
print("Raw Strings\n")

print("(r\"...\"): " + "r\"Hello\\nWorld!\" -> " + r"Hello\nWorld!")

print()