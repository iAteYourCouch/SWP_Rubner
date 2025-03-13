# Funktion zur Erzeugung einer Potenzierungsfunktion
def generate_power(exponent):
    def power(base):
        return base ** exponent

    return power  # Innere Funktion wird zurückgegeben


# Funktionen für Potenzierung erzeugen
raise_two = generate_power(2)
raise_three = generate_power(3)



def auto_marke(marke):
    def modelle(modell):
        autos = {
            "Nissan": {32: "Godzilla I", 34: "4WD", 35: "Heißt nur GT-R"},
            "Rover": {200: "Kleinwagen", 45: "Mittelklasse", 75: "Limousine"},
        }
        return autos.get(marke, {}).get(modell, "Modell nicht verfügbar")

    return modelle

nissan = auto_marke("Nissan")
rover = auto_marke("Rover")

# Tests für generate_power
#print(raise_two(4))  # 16
#print(raise_two(5))  # 25
#print(raise_three(4))  # 64
#print(raise_three(5))  # 125

#print(nissan(32))
#print(nissan(34))
#print(rover(200))
print(rover(75))
#print(rover(45))