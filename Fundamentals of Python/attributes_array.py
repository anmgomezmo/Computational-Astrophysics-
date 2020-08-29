import numpy as np

a = np.array([[1,2,3],[4,5,6],[7,8,9]])

print(a)

print(np.ndim(a))
print(a.shape)
print(a.max())
print(a.min())
print(a.sum())
print(a[0,:].sum())
print(a[:,1].sum())
print(a.mean())
