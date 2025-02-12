# Aufgabe 1: Berechnet den Durchschnitt und die Anzahl der Elemente eines Arrays mit Zahlen
def calc_1(array):
    if not array:  # Falls das Array leer ist, geben wir 0 als Durchschnitt zurück
        return 0, 0
    return sum(array) / len(array), len(array)

# Aufgabe 2: Nimmt zwei Parameter entgegen und gibt die Summe und das Produkt zurück
def calc_2(n, m):
    return n + m, n * m
