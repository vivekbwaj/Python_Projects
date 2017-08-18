import numpy as np

var=np.array([(1,3,5),(2,4,6)])

print(var)
print(type(var)) # what type var variable is
print(var.ndim)  # dimensions of the numpy array
print(var.itemsize) #bytesize of each element
print(var.dtype)  # data type of the elements
print((var.size)) #number of elements
print(var.shape) # gives (r,c) r is number of rows and c is number of columns
print(var.reshape(3,2))

var2=np.linspace(1,3,5) #Return evenly spaced numbers over a specified interval.
print(var2)
print(var.max())
print(var.min())
print(var.mean())
print(var.sum())
print(var.sum(axis=0)) #print sum of indidual columns
print(var.sum(axis=1))  # print sum of individual rows

print(np.sqrt(var))
print(np.std(var))# standard deviation

x=np.array([1,2,3])
y=np.array([4,5,6])
print(x+y)  # addition of 2 arrays

print(var.ravel())