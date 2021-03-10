# -*- coding: utf-8 -*-
"""

Gjettelek: Vi tenker på et tall, bruker
skal gjette på hvilket tall det er.

"""

from random import randint


tall = randint(1, 1000)

antall_forsøk = 10

for gjett_nr in range(1, antall_forsøk + 1):
    gjett = int(input("Hvilket tall tror du jeg tenker på? "))
    
    if gjett == tall:
        print(f"Riktig! Jeg tenkte på {tall}.")
        break
    elif gjett < tall:
        print("Dette var for lavt; prøv igjen!")
    elif gjett > tall:
        print("Det var for høyt; prøv igjen!")
else:
    print("Du klarte dessverre ikke å gjette tallet.")
    print(f"Tallet var {tall}.")



