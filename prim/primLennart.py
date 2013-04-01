# -*- coding: iso-8859-1 -*-
# Dieses Programm soll Primzahlen errechnen.


def berechnePrim(obereGrenze=10000):
    primArray = [3]
    for i in range(1,obereGrenze-1,2):
        zahl = 0
        for j in range(3,i-1,2):
            mod = i % j
            if mod == 0:
                zahl = 0
                break
            else:
                zahl = i

        if zahl != 0:
            primArray.append(zahl)
        else:
            pass

    return primArray
