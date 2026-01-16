import math

class Polynom:
    def __init__(self, coefficients):
        self.coefficients = coefficients

    def __call__(self, x):
        return sum(coef * (x ** i) for i, coef in enumerate(self.coefficients))

    def __add__(self, other):
        new_coeffs = []
        for i in range(max(len(self.coefficients), len(other.coefficients))):
            coef1 = self.coefficients[i] if i < len(self.coefficients) else 0
            coef2 = other.coefficients[i] if i < len(other.coefficients) else 0
            new_coeffs.append(coef1 + coef2)
        return Polynom(new_coeffs)

    def __sub__(self, other):
        new_coeffs = []
        for i in range(max(len(self.coefficients), len(other.coefficients))):
            coef1 = self.coefficients[i] if i < len(self.coefficients) else 0
            coef2 = other.coefficients[i] if i < len(other.coefficients) else 0
            new_coeffs.append(coef1 - coef2)
        return Polynom(new_coeffs)

class LinearFunction(Polynom):
    def __init__(self, a, b):
        super().__init__([b, a])

    def roots(self):
        a = self.coefficients[1]
        b = self.coefficients[0]
        if a == 0:
            return []
        return [-b / a]

    def __add__(self, other):
        result = super().__add__(other)
        degree = len(result.coefficients) - 1
        if degree == 1:
            return LinearFunction(result.coefficients[1], result.coefficients[0])
        elif degree == 2:
            return QuadraticFunction(result.coefficients[2], result.coefficients[1], result.coefficients[0])
        else:
            return Polynom(result.coefficients)

    def __sub__(self, other):
        result = super().__sub__(other)
        degree = len(result.coefficients) - 1
        if degree == 1:
            return LinearFunction(result.coefficients[1], result.coefficients[0])
        elif degree == 2:
            return QuadraticFunction(result.coefficients[2], result.coefficients[1], result.coefficients[0])
        else:
            return Polynom(result.coefficients)

class QuadraticFunction(Polynom):
    def __init__(self, a, b, c):
        super().__init__([c, b, a])

    def roots(self):
        a = self.coefficients[2]
        b = self.coefficients[1]
        c = self.coefficients[0]
        if a == 0:
            if b == 0:
                return []
            return [-c / b]
        discriminant = b**2 - 4*a*c
        if discriminant < 0:
            return []
        elif discriminant == 0:
            return [-b / (2*a)]
        else:
            sqrt_disc = math.sqrt(discriminant)
            return [(-b - sqrt_disc)/(2*a), (-b + sqrt_disc)/(2*a)]

    def __add__(self, other):
        result = super().__add__(other)
        degree = len(result.coefficients) - 1
        if degree == 1:
            return LinearFunction(result.coefficients[1], result.coefficients[0])
        elif degree == 2:
            return QuadraticFunction(result.coefficients[2], result.coefficients[1], result.coefficients[0])
        else:
            return Polynom(result.coefficients)

    def __sub__(self, other):
        result = super().__sub__(other)
        degree = len(result.coefficients) - 1
        if degree == 1:
            return LinearFunction(result.coefficients[1], result.coefficients[0])
        elif degree == 2:
            return QuadraticFunction(result.coefficients[2], result.coefficients[1], result.coefficients[0])
        else:
            return Polynom(result.coefficients)

f1 = LinearFunction(2, -4)   # f(x) = 2x - 4
print(f"Linear roots: {f1.roots()}")  # [2.0]

f2 = QuadraticFunction(1, -3, 2)  # f(x) = x^2 - 3x + 2
print(f"Quadratic roots: {f2.roots()}")  # [1.0, 2.0]

f3 = f1 + f2
print(f"Resulting function coefficients: {f3.coefficients}, type: {type(f3).__name__}")
print(f"Roots of the sum: {f3.roots()}")