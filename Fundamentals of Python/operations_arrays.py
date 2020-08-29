import numpy as np

a = np.random.random([3,3])

b = np.random.random([3,3])

print(a, b)

c = a + 2
print(c)

d = a + b
print(d)

e = a*b #element wiseproduct
print(e)

f = a@b #matrix product
print(f)

f = a.dot(b) #matrix product alternative
print(f)

g = a/b
print(g)

print(10*np.sin(c))

print(np.exp(d))

print(np.log10(f))

a = np.random.random([3,4])
print(a.shape)

print(a)

print(a.T) #Transpose

print(a.T.shape)

print(a.ravel()) #flattens the array

print(a.reshape(6,2)) 
