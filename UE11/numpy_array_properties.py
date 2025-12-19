import numpy as np

def list_to_numpy(lst):
    arr = np.array(lst)
    print("Array:")
    print(arr)
    print("Shape:", arr.shape)
    print("Number of dimensions:", arr.ndim)
    print()
    return arr

a1 = list_to_numpy([1, 2, 3])
a2 = list_to_numpy([[1, 2], [3, 4]])
a3 = list_to_numpy([[[1], [2]], [[3], [4]]])

original = np.array([1, 2, 3])
view = original.view()
copy = original.copy()

view[0] = 99

print("Original after modifying view:", original)
print("Copy remains unchanged:", copy)