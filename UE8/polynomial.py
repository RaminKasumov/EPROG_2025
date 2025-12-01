import math

class Polynomial:
    def __init__(self, coeffs):
        self.coeffs = coeffs
        self.degree = len(coeffs) - 1

    def eval(self, x):
        return sum(a * x**i for i, a in enumerate(self.coeffs))

    def diff(self):
        if self.degree == 0:
            return Polynomial([0])
        return Polynomial([i * a for i, a in enumerate(self.coeffs)][1:])

    def integrate(self, x1, x2):
        antider = [0] * (self.degree + 2)
        for i, a in enumerate(self.coeffs):
            antider[i+1] = a / (i+1)
        F = lambda x: sum(c * x**i for i, c in enumerate(antider))
        return F(x2) - F(x1)

    def zeros(self):
        if self.degree != 2:
            raise ValueError("Zero computation only implemented for degree 2.")
        a, b, c = self.coeffs[2], self.coeffs[1], self.coeffs[0]
        D = b*b - 4*a*c
        if D < 0:
            return None
        return (-b + math.sqrt(D)) / (2 * a), (-b - math.sqrt(D)) / (2 * a)

    @staticmethod
    def add(f1, f2):
        n = max(len(f1.coeffs), len(f2.coeffs))
        c1 = f1.coeffs + [0]*(n - len(f1.coeffs))
        c2 = f2.coeffs + [0]*(n - len(f2.coeffs))
        return Polynomial([c1[i] + c2[i] for i in range(n)])

p = Polynomial([1,2,3])
print(p.eval(2))
print(p.diff().coeffs)
print(p.integrate(0,1))