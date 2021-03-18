"""

Omvendt gjettelek: Vi skal tenke på et tall,
datamaskinen skal gjette hvilket tall det er.

"""

def midtpunkt(a, b):
    return (a + b)/2


nedre = 1
øvre = 100
antall_forsøk = 10

for i in range(1, antall_forsøk + 1):
    
    gjett = int(midtpunkt(nedre, øvre))
    
    print(f"Jeg gjetter på {gjett}")
    
    svar = input("Er det riktig? Skriv 'ja', 'for høyt' eller 'for lavt': ")
    
    if svar == "ja":
        print(f"Jeg gjettet riktig på {i} forsøk!")
        print("Jeg er en flink datamaskin!")
        break
    elif svar == "for høyt":
        øvre = gjett
    elif svar == "for lavt":
        nedre = gjett

