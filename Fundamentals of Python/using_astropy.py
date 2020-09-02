import numpy as np
import astropy.units as u
from astropy import constants as const

print(const.G, "\n\n", const.c, "\n\n", const.M_sun,
"\n\n", const.hbar, "\n\n", const.k_B, "\n\n")

print(const.c.to("pc/yr"), "\n\n", const.c.to("lyr/yr"), "\n\n")

M = 1*u.M_sun
print(M)

G = const.G
c = const.c
rS = 2*G*M/c**2
print(rS)
rS = rS.decompose()
print(rS)
print(rS.to(u.km), "\n\n")

ly = 1*u.lyr  # light year (distance travelled by light in vacuum in one julian year)
print(ly, "\n", ly.to(u.m), "\n\n")

au = 1*u.au
print(au, "\n", au.to(u.m), "\n", au.to(u.lyr), "\n\n")

def d(alpha = 1*u.arcsec, baseline = 1*u.au):
    '''
    -------------------------------------------
    d(alpha, baseline)
    -------------------------------------------
    Returns the distance to a star using the
    parallax method.

    Arguments:
    baseline in au
    parallax angle alpha given in arcsec
    -------------------------------------------
    '''
    return baseline/np.tan(alpha)

alphaCentauri_distance = d(0.75481*u.arcsec)
print(alphaCentauri_distance, "\n", alphaCentauri_distance.to(u.lyr))

pc = d(1*u.arcsec)
print(pc, "\n", pc.to(u.pc), "\n", pc.to(u.lyr), "\n")
print(d(1*u.marcsec).to(u.pc), "\n\n", alphaCentauri_distance.to(u.pc))

cygni_distance = d(0.316*u.arcsec)
print(cygni_distance, "\n", cygni_distance.to(u.pc), "\n\n")

from sympy import Symbol, solve
b = Symbol("b")
print(solve(100.-b**5, b), "\n\n") #la solucion es el primer valor del vector resultado

def M(m, D):
    '''
    -------------------------------------------
    M(m, D)
    -------------------------------------------
    Returns the absolute magnitude of a star.

    Arguments:
    m: apparent magnitude
    D: Distance to the sun in parsecs
    -------------------------------------------
    '''
    return m - 5*(np.log10(D) - 1)

D_sun = 1*u.au.to(u.pc)
print(M(-26.83, D_sun))
