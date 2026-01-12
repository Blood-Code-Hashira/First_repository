import numpy as np

temperatures = np.array([32.5, 31.8, 33.0, 35.2, 36.6])
average = np.mean(temperatures)
print(f"\nUsing np.mean :\n{average}")
print(f"\nUsing dtype :\n{temperatures.dtype}")

python_list = [1, 2, 3, 4, 5]
print("\n",python_list,"\n")

x = np.array([1, 2, 3, 4, 5])
print("\n",x,"\n")

"""
3 rows and 2 columns
"""

matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

matrix2 = np.array([[11, 21, 31],
                   [41, 51, 61],
                   [71, 81, 91]])

c = np.zeros(3)
print(f"\nUsing zeros :\n{c}")

#c1 = c.transpose()
#print(f"Using Transpose :\n{c1}")

d = np.ones(4)
print(f"\nUsing np.ones:\n{d}")

x2 = matrix.shape
print(f"\nUsing shape :\n{x2}")

x1 = matrix.dot(matrix2)
print(f"\nUsing dot :\n{x1}")

filled_array = np.full((2, 2),7)
print(f"\nUsing np.full:\n{filled_array}")


filled_array_2 = np.full((3, 3),8)
print(f"\nUsing np.full:\n{filled_array_2}")

x3 = np.arange(1, 10, 2)
print(f"\nUsing np.arange:\n{x3}")

identity = np.eye(8)
print(f"\nUsing np.eye:\n{identity}")
