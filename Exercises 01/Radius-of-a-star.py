import numpy as np
from astropy import constants as const
from astropy import units as u

def RadiusStar(L,T):
    '''
    --------------------------------------
    RadiusStar(L,T)
    --------------------------------------
    L: Luminocity in solar units
    T: Effective temperature in kelvin
    --------------------------------------
    '''
    if L > 0 and T > 0:
        R = np.sqrt((L*const.L_sun)/
        (4*np.pi*const.sigma_sb*((T*u.k)**4)*const.R_sun**2))
        return R
    elif T < 0 and L < 0:
        print("ERROR, The values of T or L should be positive.")
    elif T < 0:
        print("ERROR, The values of T should be positive in kelvin units.")
    elif L < 0:
        print("ERROR, The values of L should be positive in Whatts units.")

# Example of proxima centauri
print(RadiusStar(0.0017,3042))

print(RadiusStar(0.0017,-3042))

print(RadiusStar(-0.0017,3042))

print(RadiusStar(-0.0017,-3042))
