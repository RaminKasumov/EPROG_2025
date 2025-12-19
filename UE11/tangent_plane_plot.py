import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return x**2 + y**2

x = y = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

x0, y0 = -4, 4
Z_tangent = f(x0, y0) + 2*x0*(X - x0) + 2*y0*(Y - y0)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

ax.plot_surface(X, Y, Z, alpha=0.6, cmap='tab20')
ax.plot_surface(X, Y, Z_tangent, alpha=0.6, cmap='tab20')

ax.set_title("Function and Tangent Plane")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")

plt.show()