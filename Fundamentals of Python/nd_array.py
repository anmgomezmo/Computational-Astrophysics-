import numpy as np

a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a)
print(a[0])
print(a[1])
print(a[1,1])
print(a[1,:])
print(a[:,1])
print(a[:])

print(np.array([np.arange(3),np.arange(3),np.arange(3)]))
print(np.zeros([3,3]))
print(np.ones([4,3]))
print(np.random.random([4,3]))
