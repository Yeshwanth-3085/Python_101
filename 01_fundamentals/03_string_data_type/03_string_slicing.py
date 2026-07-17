# A slice returns a portion of a string.
# Unlike indexing, which returns one character,
# slicing can return multiple characters.
# Let's extract a word from a string

some_str = "Hello World!"
len_str = len(some_str)

print("Extracting a Portion of a String")
print("Syntax: [start:stop]")
print("Slicing starts at 'start' and stops before 'stop'")
print()

print(f"some_str = {some_str}")
print(f"len_str = {len_str}")

print("\nPositive Slicing")
print(f"some_str[0 : 5] = {some_str[0 : 5]}")
print(f"some_str[6 : len_str] = {some_str[6 : len_str]}")

print("\nNegative Slicing")
print(f"some_str[-len_str : -7] = {some_str[-len_str : -7]}")

# Negative indices stop at -1.
# To include the first character when slicing,
# use len_str or simply leave the stop blank.

print(f"some_str[-6 : len_str] = {some_str[-6 : len_str]}")

print()
print("-" * 50)
print()

print("Omitting Start or Stop Index")
print("Leaving start or stop blank defaults to the beginning or end.")
print("If start is left blank [ : 5], Slicing begins from the start")
print("If stop is left blank [6 : ], Slicing continues until the end")
print()

print(f"some_str = {some_str}")
print(f"len_str = {len_str}")

print("\nPositive Slicing")
print(f"some_str[ : 5] = {some_str[ : 5]}")
print(f"some_str[6 : ] = {some_str[6 : ]}")

print("\nNegative Slicing")
print(f"some_str[ : -7] = {some_str[ : -7]}")
print(f"some_str[-6 : ] = {some_str[-6 : ]}")

print()
print("-" * 50)
print()

# The step controls how many characters
# Python skips between each selection.

print("Slicing with Step")
print(f"some_str = {some_str}")
print(f"len_str = {len_str}")

print("\nPositive Slicing")
print(f"some_str[ : 5 : 2] = {some_str[ : 5 : 2]}")
print(f"some_str[6 : : 2] = {some_str[6 : : 2]}")

print("\nNegative Slicing")
print(f"some_str[ : -7 : 2] = {some_str[ : -7 : 2]}")
print(f"some_str[-6 : : 2] = {some_str[-6 : : 2]}")

print()
print("-" * 50)
print()


# A negative step traverses the string backwards,
# allowing us to reverse it.

print("Reversing a String")
print(f"some_str = {some_str}")
print(f"len_str = {len_str}")
print(f"some_str[::-1] = {some_str[::-1]}")

print("\nPositive Slicing")
print(f"some_str[ : 5 : -1] = {some_str[ : 5 : -1]}")
print(f"some_str[4 : : -1] = {some_str[4 : : -1]}")

print("\nNegative Slicing")
print(f"some_str[ : -7 : -1] = {some_str[ : -7 : -1]}")
print(f"some_str[-8 : : -1] = {some_str[-8 : : -1]}")