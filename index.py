import numpy as np

a = np.array([1, 2, 3])
# a = np.array([1, 2, 3], dtype='int16')

b = np.array( [ [ 9.0, 8.0, 7.0 ] , [ 6.0, 5.0, 4.0 ] ])
print(b)

# Get Dimension
a.ndim
b.ndim

# Get Shape
a.shape # (3, )
b.shape # (2, 3)

# Get Type
a.dtype # int32

# Get Size 
a.itemsize # 4
b.itemsize # 8

# Get Total Size
a.size * a.itemsize