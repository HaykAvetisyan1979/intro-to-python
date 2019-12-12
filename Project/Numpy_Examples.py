import numpy as np

w = np.array([range(0, 10, 2), range(10, 100, 20)], dtype=str)

print(w, "\n", type(w))
print(w[0, 1], w[0][1])
