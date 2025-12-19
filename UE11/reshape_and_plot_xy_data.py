import numpy as np
import matplotlib.pyplot as plt

data = np.load("file/xy1d.npy")
reshaped = data.reshape(-1, 2)

x = reshaped[:, 0]
y = reshaped[:, 1]

plt.plot(x, y, marker='o', linestyle='None')
plt.xlabel("x")
plt.ylabel("y")
plt.title("XY Data Plot")
plt.axis('equal')
plt.grid(True)
plt.show()