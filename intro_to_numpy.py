import numpy as np 

# create 1D numpy array
a = np.array([1, 2, 3, 5, 8])
# print(type(a))
# print(a.shape)
# print(a.dtype)
# print(a)

# set data type when creating numpy array
a = np.array([1, 2, 3, 5, 8], dtype='float32')
# print(a.dtype)

# access numpy array
# print(a[0], a[1], a[-1])
# print(a)

# create 2D numpy array
b = np.array([[1, 2, 3], [4, 5, 6]])
# print(b.shape)
# print(b[0, 0], b[0, 1], b[1, 0])
# print('2D matrix:', b)

# create numpy array using built-in function
c = np.ones((3, 4))
# print(c.shape)
# print('c:', c)
c = np.zeros((2,2))
# print('c:', c)

# Create a 2x2 Identity matrix
d = np.eye(4)
# print(d)
e = np.random.random((2, 2))
# print(e)

# Array Indexing
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
# print(a)
b = a[:2, 1:3]
# print(b)

# numpy masking
a = np.array([[1, 2], [3, 4], [5, 6]])

bool_idx = (a > 2)

# print(bool_idx)
# print ('using bool index:', a[bool_idx])
# print ('direct:', a[a > 2])

# Array Math
x = np.array([[1, 2], [3, 4]], dtype=np.float64)
y = np.array([[5, 6], [7, 8]], dtype=np.float64)

# Element wise sum; both produce this array
# "[[6.0 8.0]
#  [10.0 12.0]]"

# print(x+y)
# print(np.add(x, y))



# Element wise subtraction
# "[[-4.0 -4.0]
#  [-4.0 -4.0]]"

# print(x - y)
# print(np.subtract(x, y))



# Element wise multiplication
# "[[  5.  12.]
#  [ 21.  32.]]"

# print(x * y)
# print (np.multiply(x, y))



# Element wise division
# "[[ 0.2         0.33333333]
#  [ 0.42857143  0.5       ]]"

# print (x / y)
# print (np.divide(x, y))



# Element wise Square root 
# "[[ 1.          1.41421356]
#  [ 1.73205081  2.        ]]"

# print(np.sqrt(x))


# numpy reshape
a = np.arange(12)
print(a)
b = a.reshape(3, 4)
print(b)
c = a.reshape(3, 3)
print(c)