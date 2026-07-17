# A string is a sequence of characters.
# We can access individual characters using indexing.

some_str = "Hello World!"

# Positive indexing starts at 0 and moves left to right.
print("Positive Indexing (0 to len-1)")
print(f"some_str = {some_str}")
print(f"some_str[0] = {some_str[0]}")
print(f"some_str[1] = {some_str[1]}")

print()
print("-" * 50)
print()

# Negative indexing starts at -1 and moves right to left.
print("Negative Indexing (-1 to -len)")
print(f"some_str = {some_str}")
print(f"some_str[-1] = {some_str[-1]}")
print(f"some_str[-2] = {some_str[-2]}")

print()
print("-" * 50)
print()

# len() returns the length of the string
print("len() returns length (number of characters) of the string")
print(f"len(some_str) = {len(some_str)}")
print(f"First positive index = {0}")
print(f"Last positive index = {len(some_str) - 1}")
print(f"First negative index = {-1}")
print(f"Last negative index = {-len(some_str)}")

print()
print("-" * 50)
print()

# We use an index to access an individual character.
print("Accessing Characters")
print(f"some_str = {some_str}")
print(f"some_str[0] = {some_str[0]}")
print(f"some_str[-len(some_str)] = {some_str[-len(some_str)]}")

print()
print("-" * 50)
print()

# If we use an index beyond the length of the string,
# Python raises an IndexError.
print("Using Index beyond the length of the string, raises IndexError")
print(f"some_str = {some_str}")
print(f"len(some_str) = {len(some_str)}")

# We'll learn try-except later.
# For now, we're only using it to display the error.

try:
    print(f"some_str[12] = {some_str[12]}")
except IndexError as e:
    print(e)
try:
    print(f"some_str[-13] = {some_str[-13]}")
except IndexError as e:
    print(e)
