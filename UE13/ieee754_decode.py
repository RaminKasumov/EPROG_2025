"""
Given:
Sign bit = 0  → positive
Exponent bits = 00001010 = 10
Bias = 127 → actual exponent = 10 - 127 = -117
Mantissa bits = 01000000000000000000000

Mantissa value:
1 + 0/2 + 1/4 = 1.25

Final value:
1.25 * 2^-117
"""

value = 1.25 * (2 ** -117)
print(value)