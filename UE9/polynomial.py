class Polynomial:
    def __init__(self, coefficients):
        self.coeff = coefficients

    def __mul__(self, other):
        result_degree = len(self.coeff) + len(other.coeff) - 1
        result = [0] * result_degree

        for i in range(len(self.coeff)):
            for j in range(len(other.coeff)):
                result[i + j] += self.coeff[i] * other.coeff[j]

        return Polynomial(result)

    def __repr__(self):
        return f"Polynomial({self.coeff})"