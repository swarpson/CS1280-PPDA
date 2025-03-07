import numpy as np

# Creating a 1D NumPy array
data1 = [6, 7, 5, 8, 0, 1] #it is a list
arr1 = np.array(data1) # list --> converts to ndarray
print(arr1) # [6 7 5 8 0 1]
print("Type:",type(arr1)) # Type: <class 'numpy.ndarray'>
print("Shape:", arr1.shape) # Shape: (6,)
print("Size:",arr1.size) # Size: 6
print("Dimensions:", arr1.ndim) # Dimensions: 1
print("Data type:", arr1.dtype) # Data type: int64
print("Item_Size:",arr1.itemsize) # size in bytes of each element of the array.
print("total_memory: =", arr1.size * arr1.itemsize,"bytes")