class Matrix:
    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrix dimensions must match for addition.")

        result = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(self.data[i][j] + other.data[i][j])
            result.append(row)

        return Matrix(result)

    def __mul__(self, other):
        if self.cols != other.rows:
            raise ValueError("Invalid matrix dimensions for multiplication.")

        result = []
        for i in range(self.rows):
            row = []
            for j in range(other.cols):
                value = 0
                for k in range(self.cols):
                    value += self.data[i][k] * other.data[k][j]
                row.append(value)
            result.append(row)

        return Matrix(result)

    def __repr__(self):
        return f"Matrix({self.data})"