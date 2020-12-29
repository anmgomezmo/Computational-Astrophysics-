import numpy as np
from astropy import constants as const

def lorentz_gamma(par,beta=False):
    if beta:
        return 1.0/np.sqrt(1-(par*par))
    else:
        return 1.0/np.sqrt(1-(par*par)/(const.c*const.c))


def file(Nmax):
    beta = np.linspace(0,0.99999999,Nmax)
    gamma = lorentz_gamma(beta,beta=True)
    func = np.column_stack((beta,gamma))
    np.savetxt('lorentz_gamma.txt',func,fmt='%0.4f',header='Values of beta (v/c) and its respective gamma function')


N = 100
file(N)
