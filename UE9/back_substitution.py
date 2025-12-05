def back_substitution(U, b):
    try:
        n = len(U)
        x = [0] * n

        x[n - 1] = b[n - 1] / U[n - 1][n - 1]

        for i in range(n - 2, -1, -1):
            sum_val = 0
            for j in range(i + 1, n):
                sum_val += U[i][j] * x[j]

            x[i] = (b[i] - sum_val) / U[i][i]

        return x

    except ZeroDivisionError:
        print("Error: Division by zero. Matrix is singular.")
    except IndexError:
        print("Error: Invalid matrix or vector size.")
    except Exception as e:
        print("Unexpected error:", e)

# Debug tip:
# Run in terminal:
# python -m pdb back_substitution.py