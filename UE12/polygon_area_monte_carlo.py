import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path

vertices = np.load("file/vertices.npy")
polygon = Path(vertices)

xmin, ymin = vertices.min(axis=0)
xmax, ymax = vertices.max(axis=0)

N = 100000
points = np.random.uniform([xmin, ymin], [xmax, ymax], size=(N, 2))
inside = polygon.contains_points(points)

area_box = (xmax - xmin) * (ymax - ymin)
area_estimate = area_box * inside.mean()

print("Estimated area:", area_estimate)

plt.scatter(points[inside, 0], points[inside, 1], s=1)
plt.scatter(points[~inside, 0], points[~inside, 1], s=1)
plt.plot(*vertices.T, color="black")
plt.show()