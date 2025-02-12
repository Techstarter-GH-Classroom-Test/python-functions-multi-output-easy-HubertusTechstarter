# Aufgabe 1: Berechnet den Durchschnitt und die Anzahl der Elemente eines Zahlenarrays
def calc_1(array):
    if not array:  # Überprüfen, ob das Array leer ist, um Division durch Null zu vermeiden
        return None, 0
    return sum(array) / len(array), len(array)

# Aufgabe 2: Gibt die Summe und das Produkt von zwei Zahlen zurück
def calc_2(n, m):
    return n + m, n * m
