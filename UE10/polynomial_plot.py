import numpy as np
import matplotlib.pyplot as plt

class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = np.array([float(c) for c in coefficients])

    def __call__(self, x):
        arr = np.array(x)
        coefficients_high_first = self.coefficients[::-1]
        y = np.polyval(coefficients_high_first, arr)
        if arr.shape == ():
            return float(y)
        return y.tolist()

    def derivative(self):
        n = len(self.coefficients)
        if n <= 1:
            return Polynomial([0.0])
        deriv = [self.coefficients[i] * i for i in range(1, n)]
        return Polynomial(deriv)

    def plot(self, x1, x2, num=400, title=None):
        xs = np.linspace(x1, x2, num)
        ys = self(xs)
        plt.figure(figsize=(8, 5))
        plt.plot(xs, ys, label=self._label())
        plt.axhline(0, color='black', linewidth=0.7)
        plt.xlabel('x')
        plt.ylabel('p(x)')
        if title is None:
            title = f'Polynomial plot: {self._label()}'
        plt.title(title)
        plt.legend()
        plt.grid(True)
        plt.show()

    def _label(self):
        terms = []
        for i, c in enumerate(self.coefficients):
            if abs(c) < 1e-12:
                continue
            if i == 0:
                terms.append(f"{c:.3g}")
            elif i == 1:
                terms.append(f"{c:.3g}·x")
            else:
                terms.append(f"{c:.3g}·x^{i}")
        if not terms:
            return "0"
        return " + ".join(terms)

p = Polynomial([1, -2, 0, 1])
p.plot(-3, 3, title="Example: p(x) = x^3 - 2x + 1")