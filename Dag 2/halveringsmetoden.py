"""

Demonstrasjon av halveringsmetoden.

"""

from pylab import cos, sign, plot, linspace, show, grid

def f(x):
    return cos(x) - 0.1*x

def midtpunkt(a, b):
    return (a + b)/2


nedre = -6
øvre = 6

antall_gjett = 100

xverdier = linspace(nedre, øvre, 100)
plot(xverdier, f(xverdier))
grid()
show()

for gjett_nr in range(1, antall_gjett + 1):
    
    gjett = midtpunkt(nedre, øvre)
    
    print(f"Jeg gjetter på x = {gjett}")
    print(f"Da er f(x) = {f(gjett)}")
    
    verdi = f(gjett)
    
    if abs(verdi) < 0.01:
        print("Jeg fant et nullpunkt!")
        print(f"Jeg brukte {gjett_nr} antall forsøk.")
        break
    elif sign(f(nedre)) == sign(verdi):
        nedre = gjett
    else:     # sign(f(nedre)) != sign(verdi)
        øvre = gjett
    
    
    
    