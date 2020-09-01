class Planet(object):

    def __init__(self, planet_name, mass, orbit_period):
        self.planet_name = planet_name
        self.mass = mass # in units of Earth mass
        self.orbit_period = orbit_period # in Earth years
        # planet_name, mass, orbit_period are attributes (like parameters)
        # but the following is a method (like operations with parameters)
    def semimajor_axis(self): # care with the identation
        '''
        ----------------------------------------
        semimajor_axis()
        ----------------------------------------
        Returns the value of the semimajor axis
        of the planet in Au, calculated using
        Kepler's third law.
        ----------------------------------------
        '''
        return self.orbit_period**(2./3.)

mars = Planet("Mars", 0.107, 1.88)
print(mars.mass, mars.orbit_period)
print(mars.semimajor_axis())

earth = Planet("Earth", 1., 1.)
print(earth.mass, earth.orbit_period)
print(earth.semimajor_axis())

print(Planet.semimajor_axis.__doc__)

print("\n\n")

class Dwarf(Planet):
    def description(self):
        '''
        ----------------------------------------
        description()
        ----------------------------------------
        Returns a string with the information
        of the mass of the dward planet.
        ----------------------------------------
        '''
        descrip = self.planet_name + " is a dwarf planet with a mass of " \
        + str(self.mass) + " Earth masses."
        return descrip

pluto = Dwarf("Pluto", 0.00218, 248.00)
print(pluto.mass, pluto.semimajor_axis(), pluto.description())
