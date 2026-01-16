"""
Largest normalized positive number:
Mantissa = 1.111 (binary) = 1 + 1/2 + 1/4 + 1/8 = 1.875
Exponent = 4
Value = 1.875 * 2^4 = 30.0

Smallest normalized positive number:
Mantissa = 1.000
Exponent = -4
Value = 1.0 * 2^-4 = 1/16 = 0.0625

Smallest non-normalized positive number:
Mantissa = 0.001
Exponent = -4
Value = (1/8) * 2^-4 = 2^-7 = 0.0078125

2.75 in binary:
2.75 = 10.11₂ = 1.011₂ * 2^1
Mantissa = 1.011
Exponent = 1
"""

def float_to_floating_point(x):
    best_val = None
    best_err = None

    for e in range(-4, 5):
        for m in range(8, 16):
            val = (m * (2 ** e)) / 8
            err = abs(x - val)

            if best_err is None or err < best_err:
                best_err = err
                best_val = val

    return best_val