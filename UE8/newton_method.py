def newton(f, fprime, x0, tol=1e-7, max_iter=1000):
    x_prev = x0
    for i in range(max_iter):
        fx = f(x_prev)
        fpx = fprime(x_prev)

        if abs(fpx) <= tol * abs(fx):
            raise ValueError("Derivative too small — method fails.")

        x_new = x_prev - fx / fpx

        if abs(fx) < tol or abs(x_new - x_prev) < tol:
            return x_new

        x_prev = x_new

    raise ValueError("Newton method did not converge.")

# Working example:
f = lambda x: x**2 - 2
fp = lambda x: 2*x
print(newton(f, fp, 1))

# Failing example:
f_fail = lambda x: x**(1/3)
fp_fail = lambda x: (1/3)*x**(-2/3)