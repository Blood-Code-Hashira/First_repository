import numpy as np

arr_2d = np.array([[1, 2, 3],
                   [4, 5, 6.]])

print(arr_2d.shape)
print(arr_2d.size)
print(arr_2d.ndim)
print(arr_2d.reshape(3, 2))
print(arr_2d.ndim)
print(arr_2d.dtype)

print(arr_2d.astype(int))
print(arr_2d.dtype)

print(arr_2d + 2)
print(arr_2d - 2)
print(arr_2d * 2)
print(arr_2d / 2)
print(arr_2d ** 2)
print(arr_2d // 2)
print(arr_2d % 2)

print(np.sum(arr_2d))
print(np.mean(arr_2d))
print(np.max(arr_2d))
print(np.min(arr_2d))
print(np.std(arr_2d))
print(np.var(arr_2d))
