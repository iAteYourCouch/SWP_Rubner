import random

def main():
    print()


numbers = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
farben = ("Kreuz", "Raute", "Herz", "Pik")

# Tuple von Pokerkarten als kartesisches Produkt - kann sich nicht ändern imutable
deck_of_cards = tuple((number, farbe) for farbe in farben for number in numbers)


# //Funktion
def get_card(index):
    number = numbers[index % 13]  # Das gibt den Wert der Karte basierend auf ihrem Modulo 13-Ergebnis
    farbe = farben[index // 13]  # Das teilt den Index durch 13, um die Farbe zu bestimmen

    return number, farbe


# Ausgabe

# Zufällige Indizes für fünf Karten generieren
random_indices = random.sample(range(52), 5)  # Sample nimmt 5 eindeutige Indizes aus dem Bereich von 0 bis 51

# Fünf zufällige Karten basierend auf den generierten Indizes
karte1 = get_card(random_indices[0])
karte2 = get_card(random_indices[1])
karte3 = get_card(random_indices[2])
karte4 = get_card(random_indices[3])
karte5 = get_card(random_indices[4])


# Ausgabe der zufälligen Karte
print("Zufällige Karte:", karte1)
print("Zufällige Karte:", karte2)
print("Zufällige Karte:", karte3)
print("Zufällige Karte:", karte4)
print("Zufällige Karte:", karte5)


#HÜ: Liste mit karten
#Zufallszahl herausholen
#Gleiche symbole % 13 um herauszufinden ob die farbe gleich ist
#Methode die checkt ob es ein flush ist oder nicht (true/false)
#Die methoden der häufigkeit nach sortieren.
#Wenn das am wenigst wahrscheinliche getroffen wird  - abbrechen
#counter


if __name__ == '__main__':
    main()
