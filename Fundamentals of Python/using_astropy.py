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
print(rS.to(u.km))
