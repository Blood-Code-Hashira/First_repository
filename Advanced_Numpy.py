import numpy as np

"""

np.insert(array, index, value, axis=0, 1)
axis = 0 Row Wise
axis = 1 Column Wise

"""

arr = np.array([10, 20, 30, 40, 50, 60, 70])
x = np.insert(arr, 7, 80, axis = 0) # Inserting
print(x)

y = np.insert(arr, 2, 25, axis = 0)
print(y)

arr_2d = np.array([[1, 2], 
                   [3, 4]])

c = np.insert(arr_2d, 1, [5, 6], axis = 0)
print(c)

d = np.insert(arr_2d, 2, [5, 6], axis = 0)
print(d)

d_2 = np.insert(arr_2d, 0, [5, 6], axis = 0)
print(d_2)

d_3 = np.insert(arr_2d, 1, [5, 6], axis = 1)
print("\nColumn Wise\n",d_3)

d_4 = np.insert(arr_2d, 1, [5, 6], axis = None)
print("\nNONE\n",d_4)

e = np.array([1, 2, 3, 4, 5, 6])
b = np.append(e, 7)
print(b)

arr_1 = np.array([1, 2, 3])
arr_2 = np.array([4, 5, 6])
o = np.concatenate((arr_1, arr_2), axis = 0)
print(o)

t = np.array([10, 20, 30, 40, 50])
t1 = np.delete(t, 0, axis = None)
print(t1)

t2 = np.array([[1, 2, 3],
              [4, 5, 6]])

t4 = np.delete(t2, 0, axis = 0)
print(t4)

t5 = np.array([1, 2, 3])
t6 = np.array([4, 5, 6])
        

print(np.vstack((t5, t6)))
print(np.hstack((t5, t6)))

t7 = np.array([[10, 20, 30, 40, 50, 60],
              [70, 80, 90, 100, 110, 120]])
print("\nEqual Splitting :\n",np.split(t7, 2))
print("\nHorizontal Splitting\n",np.hsplit(t7, 3))
print("\nVertical Splitting :\n",np.vsplit(t7, 2))

