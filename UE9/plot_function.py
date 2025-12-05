import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 400)
y = np.sin(x)

plt.plot(x, y)
plt.title("Plot of f(x) = sin(x)")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.show()