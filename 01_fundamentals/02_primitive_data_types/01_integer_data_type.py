# integer: Basically whole numbers
# negative whole numbers, zero, positive whole numbers

a = -10
b = 0
c = 10

print("Integer Data Type")
print(a, b, c)
print(type(a), type(b), type(c))
print()
print("-" * 50)
print()

# integer supports base system
# Decimal (base 10), Binary (base 2), Octal (base 8), Hexadecimal (base 16)
decimal = 10       # Decimal (base 10)
binary = 0b1010   # Binary (base 2)
octal = 0o12     # Octal (base 8)
hexadecimal = 0xA      # Hexadecimal (base 16)
print("Integer Base System")
print(decimal, binary, octal, hexadecimal)

# base conversion
print(decimal, bin(decimal), oct(decimal), hex(decimal), "  Decimal to other bases") # decimal to other bases
print(decimal, int("0b1010", 2), int("0o12", 8), int("0xA", 16), "  Other bases to decimal") # other bases to decimal
print()
print(type(decimal), type(binary), type(octal), type(hexadecimal))
print()
print("-" * 50)
print()


# python integers are insane, they can store huge numbers
# and are not limited by 32 bit or 64 bit like other languages
print("Python integers are insane, they can store huge numbers")
huge = 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
print(huge)
print(type(huge))