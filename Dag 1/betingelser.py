# -*- coding: utf-8 -*-
"""

Program som sjekker om et tall går opp i gitte faktorer.

"""

tall = 15
faktor = 5
faktor2 = 3

print(tall % faktor)
print(faktor % tall)

if ((tall % faktor) == 0) and ((tall % faktor2) == 0):
    print(f"Tallet {tall} går opp i både {faktor} og {faktor2}.")
elif (tall % faktor) == 0:
    print(f"Tallet {tall} går opp i {faktor}.")
elif (tall % faktor2) == 0:
    print(f"Tallet {tall} går opp i {faktor2}.")
else:
    print(f"Tallet {tall} går hverken opp i {faktor} eller {faktor2}.")