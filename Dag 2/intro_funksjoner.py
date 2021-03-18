"""

Introduksjon til funksjoner

"""

from math import pi

def kulevolum(radius):
    return 4/3*pi*radius**3

radius = 4

print(kulevolum(radius))

radius_golfball = 2   # cm
radius_fotball = 22   # cm
radius_jordklode = 6371  # km

volum_golfball = kulevolum(radius_golfball)
volum_fotball = kulevolum(radius_fotball)
volum_jordklode = kulevolum(radius_jordklode)

print(f"Volumet av en golfball er {volum_golfball:.2f} cm^3.")
print(f"Volumet av en fotball er {volum_fotball:.2f} cm^3.")
print(f"Volumet av en jordklode er {volum_jordklode:.2g} km^3.")


