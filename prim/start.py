 # -*- coding: iso-8859-1 -*-
# Dieses Programm vergleicht die verschiedenen für die Primzahlberechnung.
# @author Lennart
# @Version 1.4.13

# Laden der Module (eure Programme)
import primLennart
import primTill
import primChristian
import primJannis
# Modul zum Zeit messen.
import time

def vergleich(obereGrenze=10000):
    """
    Es wird ein Vergleich zwischen den Verschiedenen Algorithmen nach deren
    Berechnungsdauer geroffen.
    @param obereGrenze Die obere Grenze der zu prüfenden Zahlen.
    Defaultwer ist 10000
    """
    time.sleep(3)

    # Ausführen von Lennarts Methode und speicherns seines Arrays als
    # Vergleichsarray
    print "Führe Lennarts Algorithmus aus."
    start = time.time()
    lennartArray = primLennart.berechnePrim(obereGrenze)
    end = time.time()
    print "Berechnungszeit: ", end - start

    time.sleep(3)
    print "----------"

    print "Führe Tills Algorithmus aus."
    start = time.time()
    tillArray = primTill.berechnePrim(obereGrenze)
    end = time.time()
    print "Berechnungszeit: ", end - start
    if set(lennartArray) == set(tillArray):
        print "Die liste stimmt mit Lennarts überein"
    else:
        print "Die liste stimmt mit Lennarts NICHT überein"


    time.sleep(3)
    print "----------"

    print "Führe Jannis Algorithmus aus."
    start = time.time()
    jannisArray = primJannis.berechnePrim(obereGrenze)
    end = time.time()
    print "Berechnungszeit: ", end - start
    if set(lennartArray) == set(jannisArray):
        print "Die liste stimmt mit Lennarts überein"
    else:
        print "Die liste stimmt mit Lennarts NICHT überein"


    time.sleep(3)
    print "----------"

    print "Führe Christians Algorithmus aus."
    start = time.time()
    christianArray = primChristian.berechnePrim(obereGrenze)
    end = time.time()
    print "Berechnungszeit: ", end - start
    if set(lennartArray) == set(christianArray):
        print "Die liste stimmt mit Lennarts überein"
    else:
        print "Die liste stimmt mit Lennarts NICHT überein"


# Ausführen der Methode:
print "Bitte die obere Berechnungsgrenze angeben und Enter drücen."
berechnungsGrenze = int(input())
vergleich(berechnungsGrenze)
