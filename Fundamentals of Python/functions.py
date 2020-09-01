def myfunction(x):
    return x**2+5

print(myfunction(2.))

a = 3.

print(myfunction(a))

print("\n")

def myfunction2(x,y):
    return x**2 + y

print(myfunction2(2.,3.))

r = myfunction2(5.,1.)
print(r)

print("\n")

def myfunction3(x,y):
    r1 = x**2
    r2 = x + y
    return r1, r2

print(myfunction3(2., 3.))

a, b = myfunction3(3.,2.)
print(a)
print(b)

print("\n")

def myfunction4(x, y, z = 5):
    r2 = x**2 + y**2 + z**2
    return r2

print(myfunction4(1., 2.))
print(myfunction4(1., 2., 3.))
print(myfunction4(y = 2., x = 2., z = 0.))

print("\n\n")

def LorentzGamma(v):
    '''
    --------------------------------------
    LorentzGamma(v)
    --------------------------------------
    Receives a speed v in units of m/s
    and returns the corresponding value
    of the Lorentz gamma function in
    special relativity.
    --------------------------------------
    '''
    import numpy as np
    c = 3E8 # speed of light in m/s
    g = 1/np.sqrt(1-(v**2)/(c**2))
    return g

print(LorentzGamma(0))
print(LorentzGamma(30000))
print(LorentzGamma.__doc__)
# print(LorentzGamma?)

print("\n\n")
