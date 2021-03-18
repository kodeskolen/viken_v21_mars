
"""

Program som demonstrerer plotting.


"""

from pylab import *        # samme som numpy + matplotlib.pyplot


def kulevolum(radius):
    return 4/3*pi*radius**3

#radiusverdier = linspace(0, 100, 101)
radiusverdier = arange(0, 100, 1)

# print(radiusverdier)

volumverdier = kulevolum(radiusverdier)

plot(radiusverdier, volumverdier)
xlabel("Radius")
ylabel("Volum")

xlim(0, 100)
ylim(0, 4e6)

savefig("plott_radius.png")

show()

