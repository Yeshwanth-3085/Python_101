# A complex number has two parts:
# Real part → like normal integers or floats.
# Imaginary part → multiplied by j in Python (instead of i from math).

import math

a = 3 + 4j

print("Complex Data Type")

print(f"{a} : {type(a)}")
print(f"Real part: {a.real}, Type: {type(a.real)}")
print(f"Imaginary part: {a.imag}, Type: {type(a.imag)}")

print(f"Magnitude: {abs(a)}, Type: {type(abs(a))}")
print(f"Conjugate: {a.conjugate()}, Type: {type(a.conjugate())}")

print()
print("-" * 50)
print()

# Complex Conversions
# Rectangular -> Polar (degrees)
print("Complex Conversion: Rectangular -> Polar (degrees)")

r = abs(a)
theta_rad = math.atan2(a.imag, a.real)
theta = math.degrees(theta_rad)

print(f"{a} : {r} ∠{theta}")
print()

# Polar -> Rectangular
print("Complex Conversion: Polar -> Rectangular")

b = complex(r * math.cos(theta_rad), r * math.sin(theta_rad))
print(f"{r} ∠{theta} : {b}")