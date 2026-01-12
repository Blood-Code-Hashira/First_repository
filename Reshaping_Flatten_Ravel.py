import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])
x = arr.reshape(2, 3)
print(x)

ar_2 = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9],
                 [10, 11, 12]])
y = ar_2.reshape(3, 4)

print(y)
print(y)
# Ravel -> View
# Flatten -> Copy
c = ar_2.ravel()#It effect on the real array
print(c)
print(y)
d = ar_2.flatten()#Returns copy and do not effect on real array.
print(d)