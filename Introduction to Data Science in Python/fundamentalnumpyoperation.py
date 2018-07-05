import numpy as np

mylist = [1, 2, 3]
x = np.array(mylist)
x
y = np.array([4, 5, 6])
y
multidimarray = np.array([[7, 8, 9], [10, 11, 12]])
multidimarray

multidimarray.shape
n = np.arange(0, 30, 2)
n
n = n.reshape(3, 5)
n
# linspace is similar to arange, except you tell it how many digits to return and it would return the digits.
o = np.linspace(0, 4, 9)
o
o.resize(3, 3)

np.ones([3, 3])
np.zeros([3, 3])
np.eye(4)
#array([[1., 0., 0., 0.],
#      [0., 1., 0., 0.],
#       [0., 0., 1., 0.],
#       [0., 0., 0., 1.]])
# y = array([4, 5, 6])
np.diag(y)
#array([[4, 0, 0],
#       [0, 5, 0],
#       [0, 0, 6]])

np.array([1, 2, 3] * 3)
#array([1, 2, 3, 1, 2, 3, 1, 2, 3])

np.repeat([1, 2, 3], 3)
#array([1, 1, 1, 2, 2, 2, 3, 3, 3])
p = np.ones([3, 3], int)
#array([[1, 1, 1],
#       [1, 1, 1],
#       [1, 1, 1]])

np.vstack([p, 2*p])
np.hstack([p, 2*p])


##Common Mathematical Operation
#x = array([1, 2, 3])
#y= array([4, 5, 6])
x + y
#array
x * y
#array([ 4, 10, 18])
x**2
#array([1, 4, 9], dtype=int32)
x.dot(y)
# Via Matrix multiplication = 32

z = np.array([y, y**2])
#array([[ 4,  5,  6],
#       [16, 25, 36]])

z.shape
#(2, 3)
z.reshape(3, 2)
#array([[ 4,  5],
#       [ 6, 16],
#       [25, 36]])

#Transpose
z.T
#array([[ 4, 16],
#       [ 5, 25],
#       [ 6, 36]])
z.T.shape
#(3, 2)

z.dtype
#dtype('int32')

z = z.astype('f')
z.dtype
#dtype('float32')

#Maths function in numpy

a = np.array([-4, -3, -2, 1, 2, 3])
a.max()
a.sum()
a.min()

#index of maximum value in the array
a.argmax()
#index of minimum value in the array
a.argmin()

#Indexing and Slicing
s = np.arange(13)**2
s
#array([  0,   1,   4,   9,  16,  25,  36,  49,  64,  81, 100, 121, 144],
#      dtype=int32)

#slicing s[startindex:endindex:stepsize]
s[0], s[4], s[0:3]
#0, 16, array([0, 1, 4], dtype=int32))
s[0:3:2]
#array([0, 4], dtype=int32)
s[1:5]
#array([ 1,  4,  9, 16], dtype=int32)
s[-4:]
#array([ 81, 100, 121, 144], dtype=int32)

#slicing s[startindex:endindex:stepsize]
# this actually gets the array in reverse order (with negative step size )
s[-5::-2]

r = np.arange(36)
r = r.reshape(6, 6)
#or r.resize(6, 6) - this can reshape the array in place no assignment requirement as the above line.

#array([[ 0,  1,  2,  3,  4,  5],
#       [ 6,  7,  8,  9, 10, 11],
#       [12, 13, 14, 15, 16, 17],
#       [18, 19, 20, 21, 22, 23],
#      [24, 25, 26, 27, 28, 29],
#       [30, 31, 32, 33, 34, 35]])

# get 3 column value from 3rd row.
r[2, 2]

# get 4th row and column 3 to 6
r[3, 3:6]
#array([21, 22, 23])

#select first 2 rows and all the column values except the last column
r[:2, :-1]
#array([[ 0,  1,  2,  3,  4],
#       [ 6,  7,  8,  9, 10]])

#select every 2nd element from last rows
r[-1, ::2]
#array([30, 32, 34])

#Get array where elements in greater than specified number
r[r > 30]
#array([31, 32, 33, 34, 35])

#below assignment assigns the array values which are > 30 with the substituted value
r[r > 30] = 30
r
'''
array([[ 0,  1,  2,  3,  4,  5],
#       [ 6,  7,  8,  9, 10, 11],
#       [12, 13, 14, 15, 16, 17],
#       [18, 19, 20, 21, 22, 23],
#      [24, 25, 26, 27, 28, 29],
#      [30, 30, 30, 30, 30, 30]])
'''

# gets first 3 row and first 3 column from array r
r2 = r[0:3, 0:3]

'''
array r2 still holds a reference to array r
therefore any digit change in r2 will be reflected in r
e.g. 
r2[:] = 0 # assign all values in r2 matrix to 0
r would have first 3 rows and 3 column values set to 0
now to avoid this we need to copy the array r

'''

r2 = r.copy()
r2[:3, :3] = 0
r2

'''
array([[ 0,  0,  0,  3,  4,  5],
       [ 0,  0,  0,  9, 10, 11],
       [ 0,  0,  0, 15, 16, 17],
       [18, 19, 20,  0, 22, 23],
       [24, 25, 26, 27, 28, 29],
       [30, 30, 30, 30, 30, 30]])
'''
# matrix r remains intact
r
'''
array([[ 0,  1,  2,  3,  4,  5],
       [ 6,  7,  8,  9, 10, 11],
       [12, 13, 14, 15, 16, 17],
       [18, 19, 20, 21, 22, 23],
       [24, 25, 26, 27, 28, 29],
       [30, 30, 30, 30, 30, 30]])
'''
#Iterating over arrays
#Create a 4*3 array of random integers between 0 to 10
test = np.random.randint(0, 10, (4, 3))
test
'''
array([[2, 7, 2],
       [2, 4, 3],
       [0, 2, 7],
       [6, 5, 0]])
'''

for row in test:
    print(row)
'''
[2, 7, 2]
[2, 4, 3]
[0, 2, 7]
[6, 5, 0]
'''

for i in range(len(test)):
    print(test(i))
'''
[2, 7, 2]
[2, 4, 3]
[0, 2, 7]
[6, 5, 0]
'''

for i, row in enumerate(test):
    print("row {} is {}".format(i, row))

"""
row 0 is [2 7 2]
row 1 is [2 4 3]
row 2 is [0 2 7]
row 3 is [6 5 0]
"""

test2 = test**2

#To iterate over both arrays together (test and test2) use zio

for i, j in zip(test, test2):
    print(" {} + {} = {}".format(i, j, i + j))
'''
[2 7 2] + [ 4 49  4] = [ 6 56  6]
 [2 4 3] + [ 4 16  9] = [ 6 20 12]
 [0 2 7] + [ 0  4 49] = [ 0  6 56]
 [6 5 0] + [36 25  0] = [42 30  0]
'''

'''
test array
array([[4, 9, 1, 9, 0, 0],
       [2, 9, 5, 3, 6, 7],
       [8, 6, 9, 4, 2, 7],
       [9, 3, 9, 6, 6, 1],
       [5, 1, 1, 4, 9, 5],
       [5, 8, 2, 3, 1, 9]])

to get [9, 4
        9, 6]
array
test[2:4, 2:4]

to get all elements present in the diagonal
test.reshape(36)[::7]
'''

