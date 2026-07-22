# String Operations

# String concatenation: The '+' operator combines two or more strings.
print("String Concatenation")
some_str_1 = "Hello"
some_str_2 = "World!"
print(f"some_str_1 = {some_str_1}")
print(f"some_str_2 = {some_str_2}")
print(f"some_str_1 + ' ' + some_str_2 = {some_str_1 + ' ' + some_str_2}")

print()
print("-" * 50)
print()

# String repetition: The '*' operator repeats a string a specified number of times.
print("String Repetition")
print(f"some_str_1 * 3 = {some_str_1 * 3}")

print()
print("-" * 50)
print()

# The 'in' operator checks whether a substring
# or character exists in a string.
print("Membership (in)")
print(f"some_str_1 = {some_str_1}")
print(f"'H' in some_str_1 = {'H' in some_str_1}")
print(f"'W' in some_str_1 = {'W' in some_str_1}")

print()
print("-" * 50)
print()

# The 'not in' operator checks whether a substring
# or character does not exist in a string.
print("Non-Membership (not in)")
print(f"some_str_1 = {some_str_1}")
print(f"'H' not in some_str_1 = {'H' not in some_str_1}")
print(f"'W' not in some_str_1 = {'W' not in some_str_1}")

print()
print("-" * 50)
print()

# String Comparisons
# Strings can be compared using comparison operators.
print("String Comparisons")
print(f"some_str_1 = {some_str_1}")
print(f"some_str_2 = {some_str_2}")
print()
print(f"some_str_1 == 'Hello' = {some_str_1 == 'Hello'}")
print(f"some_str_1 == some_str_2 = {some_str_1 == some_str_2}")
print()
print(f"some_str_1 != 'Hello' = {some_str_1 != 'Hello'}")
print(f"some_str_1 != some_str_2 = {some_str_1 != some_str_2}")
print()
print(f"some_str_1 > 'Hello' = {some_str_1 > 'Hello'}")
print(f"some_str_1 > some_str_2 = {some_str_1 > some_str_2}")
print()
print(f"some_str_1 < 'Hello' = {some_str_1 < 'Hello'}")
print(f"some_str_1 < some_str_2 = {some_str_1 < some_str_2}")
print()
print(f"some_str_1 >= 'Hello' = {some_str_1 >= 'Hello'}")
print(f"some_str_1 >= some_str_2 = {some_str_1 >= some_str_2}")
print()
print(f"some_str_1 <= 'Hello' = {some_str_1 <= 'Hello'}")
print(f"some_str_1 <= some_str_2 = {some_str_1 <= some_str_2}")

print()
print("-" * 50)
print()

# Built-in Functions
sample_str = "zebra"
print("Common Built-in Functions")
print(f"sample_str = {sample_str}")

# len() returns the length of the string
print("\nlen()")
print(f"len(sample_str) = {len(sample_str)}")

# min() returns the smallest character
# according to character ordering.
print("\nmin()")
print(f"min(sample_str) = {min(sample_str)}")

# max() returns the largest character
# according to character ordering.
print("\nmax()")
print(f"max(sample_str) = {max(sample_str)}")

# sorted() returns a sorted list
# of the string's characters.
print("\nsorted()")
print(f"sorted(sample_str) = {sorted(sample_str)}")