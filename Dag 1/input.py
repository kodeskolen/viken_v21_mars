"""

Demonstrasjon av hvordan få input fra bruker.
Lite program som regner ut arealet av en sirkel!

"""


from math import pi


radius = float(input("Skriv inn radius av sirkelen: "))

#print(type(radius))
#print(type(pi))

areal = pi*radius**2

print(f"Arealet av sirkelen er {areal:.2f}")