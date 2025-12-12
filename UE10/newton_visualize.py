import numpy as np
import matplotlib.pyplot as plt

def newton_steps(f, df, x0, tol=1e-10, max_iter=50):
    x = x0
    yield x
    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)
        if abs(fx) < tol:
            return
        if dfx == 0:
            raise ValueError("Derivative zero at iterate.")
        x = x - fx / dfx
        yield x

def plot_newton_sequence(f, df, x0, x_range=None, num=400):
    xs = list(newton_steps(f, df, x0))
    if x_range is None:
        x_min = min(xs) - 1.5 * abs(xs[0] - xs[-1]) - 1
        x_max = max(xs) + 1.5 * abs(xs[0] - xs[-1]) + 1
    else:
        x_min, x_max = x_range
    xs_domain = np.linspace(x_min, x_max, num)
    ys = np.vectorize(f)(xs_domain)

    plt.figure(figsize=(9,6))
    plt.plot(xs_domain, ys, label="f(x)")
    plt.axhline(0, color='black', linewidth=0.7)

    for k, xk in enumerate(xs):
        yk = f(xk)
        dyk = df(xk)
        tangent = f(xk) + dyk * (xs_domain - xk)
        plt.plot(xs_domain, tangent, linestyle='--', alpha=0.6, label=f"Tangent at x_{k}" if k<4 else None)
        plt.scatter([xk], [yk], color='blue', s=30)
        if dyk != 0:
            xroot = xk - yk / dyk
            plt.scatter([xroot], [0.0], color='red', s=40)
            plt.annotate(f"x_{k}", xy=(xk, yk), xytext=(xk, yk + (0.08*(max(ys)-min(ys)))), fontsize=8)

    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title(f"Newton iterations starting at x0 = {x0}")
    plt.legend(loc='best', fontsize=8)
    plt.grid(True)
    plt.show()

f = lambda x: x**3 - x - 2
df = lambda x: 3*x**2 - 1
plot_newton_sequence(f, df, x0=2, x_range=(0, 2.5))