"""

Program som kombinerer løkker og betingelser.

"""

faktor = 3
faktor2 = 5


for tall in range(1, 101):
    #print(tall)

    if ((tall % faktor) == 0) and ((tall % faktor2) == 0):
        print(f"Tallet {tall} går opp i både {faktor} og {faktor2}.")
    elif (tall % faktor) == 0:
        print(f"Tallet {tall} går opp i {faktor}.")
    elif (tall % faktor2) == 0:
        print(f"Tallet {tall} går opp i {faktor2}.")
    else:
        print(f"Tallet {tall} går hverken opp i {faktor} eller {faktor2}.")


