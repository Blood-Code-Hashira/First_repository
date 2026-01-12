import numpy as np

arr = np.array([1, 2, np.nan, 4, np.nan, 6])
print(np.isnan(arr))

print(np.nan_to_num(arr, nan))
print(np.nan_to_num(arr, nan=3))

i = np.array([1, 2, np.inf, 4, -np.inf, 6])
print(np.isinf(i))

x = np.nan_to_num(i, posinf=1000, neginf=-1000)
print(x)
