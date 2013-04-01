# -*- coding: iso-8859-1 -*-
# Dieses Programm soll Primzahlen errechnen.


def berechnePrim(obereGrenze=10000):
    """
    Diese Methode prüft welche Primzahlen im Intervall 0 und obereGrenze
    liegen. 0 und 1 sind keine Primzahlen

    @param obereGrenze Gibt die obere Grenze der zu prüfenden Zahlen an.
    Der Defaultwert ist 10000"
    """
    # Ein leeres Array wird initialisiert.
    primArray = []

    """
    Hier passiert die Action.
    Es soll ein Array an Primzahlen bis zu einer gesetzen oberen Grenze
    berechnet werden.
    Also sowas wie:
    """
    erstePrimzahl = 1+1
    # An das Array anhängen
    primArray.append(erstePrimzahl)

    zweitePrimzahl = 5+3
    # An das Array anhängen
    primArray.append(zweitePrimzahl)


    return primArray
