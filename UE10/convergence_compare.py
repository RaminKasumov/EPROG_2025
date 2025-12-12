import numpy as np
import matplotlib.pyplot as plt

def bisection_steps(f, a, b, tol=1e-10, max_iter=100):
    fa = f(a)
    fb = f(b)
    if fa * fb > 0:
        raise ValueError("f(a) and f(b) must have opposite signs.")
    steps = []
    for i in range(max_iter):
        c = 0.5*(a + b)
        steps.append(c)
        fc = f(c)
        if abs(fc) < tol or (b - a)/2 < tol:
            break
        if fa * fc <= 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
    return steps

def newton_steps_list(f, df, x0, tol=1e-10, max_iter=100):
    x = x0
    steps = [x]
    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)
        if abs(fx) < tol:
            break
        if dfx == 0:
            raise ValueError("Derivative zero.")
        x = x - fx/dfx
        steps.append(x)
    return steps

def plot_sequences(seq1, seq2, label1="Bisection", label2="Newton", true_root=None):
    it1 = np.arange(len(seq1))
    it2 = np.arange(len(seq2))
    plt.figure(figsize=(9,5))
    plt.plot(it1, seq1, marker='o', label=label1)
    plt.plot(it2, seq2, marker='x', label=label2)

    if true_root is None:
        return
    else:
        plt.axhline(true_root, color='gray', linewidth=0.7, linestyle='--', label='true root')

    plt.xlabel('Iteration')
    plt.ylabel('Approximation')
    plt.title('Convergence: approximations per iteration')
    plt.legend()
    plt.grid(True)
    plt.show()

    e1 = np.abs(np.array(seq1) - true_root)
    e2 = np.abs(np.array(seq2) - true_root)
    plt.figure(figsize=(9,5))
    plt.semilogy(it1, e1, marker='o', label=label1)
    plt.semilogy(it2, e2, marker='x', label=label2)
    plt.xlabel('Iteration')
    plt.ylabel('Absolute error (log scale)')
    plt.title('Convergence: absolute error (log scale)')
    plt.legend()
    plt.grid(True, which='both')
    plt.show()

f = lambda x: x**3 - x - 2
df = lambda x: 3*x**2 - 1
bis_steps = bisection_steps(f, 1, 3, max_iter=50)
newt_steps = newton_steps_list(f, df, 2, max_iter=20)
true_root = bis_steps[-1]
plot_sequences(bis_steps, newt_steps, true_root=None)

f2 = lambda x: np.cos(x) - x
df2 = lambda x: -np.sin(x) - 1
bis2 = bisection_steps(f2, 0, 1, max_iter=60)
newt2 = newton_steps_list(f2, df2, x0=0.5, max_iter=40)
plot_sequences(bis2, newt2, label1="Bisection (cos-x)", label2="Newton (cos-x)", true_root=bis2[-1])