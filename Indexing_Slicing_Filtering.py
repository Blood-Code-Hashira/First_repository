import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60, 70])
print(arr[0]) #Indexing
print(arr[1])
print(arr[-1])
print(arr[:3])
print(arr[0:3]) #Slicing
print(arr[1:3])
print(arr[0:6:2])
print(arr[0:7:2])
print(arr[::3])
print(arr<=70)
print(arr%2)
print(arr/3)
print(arr[arr < 70]) #Filtering
