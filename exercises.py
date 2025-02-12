# Aufgabe 1: Berechnet den Durchschnitt und die Anzahl der Elemente eines Arrays mit Zahlen
def calc_1(array):
    if not array:  # Falls das Array leer ist, soll None zurückgegeben werden (laut Test)
        return None
    return sum(array) / len(array), len(array)

# Aufgabe 2: Nimmt zwei Parameter entgegen und gibt die Summe und das Produkt zurück
def calc_2(n, m):
    return n + m, n * m
