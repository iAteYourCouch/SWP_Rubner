class messung:
    def __init__(self, value, einheit, name):
        self.value = value
        self.einheit = einheit
        self.name = name

    def __str__(self):
        return f"Wert: {self.value}, Einheit: {self.einheit}, Name: {self.name}"

class temperatur(messung):
    def __init__(self, value, einheit, name, tempWert):
        super().__init__(value, einheit, name)
        self.tempWert = tempWert

    def __str__(self):
        return f"Temperatur-Sensor - Name: {self.name}, Temperatur: {self.tempWert} {self.einheit}"

class moisty(temperatur):
    def __init__(self, value, einheit, name, tempWert, feuchtPro):
        super().__init__(value, einheit, name, tempWert)
        self.feuchtPro = feuchtPro

    def __str__(self):
        return f"Feuchtigkeitssensor - Name: {self.name}, Temperatur: {self.tempWert} {self.einheit}, Feuchte: {self.feuchtPro}%"

def main():
    t1 = temperatur(1, "°C", "Sensor 1", 25)
    t2 = temperatur(2, "°C", "Sensor 2", 19)
    t3 = temperatur(3, "°C", "Sensor 3", 30)

    f1 = moisty(1, "°C", "Feuchti 1", 25, 60)
    f2 = moisty(2, "°C", "Feuchti 2", 0, 10)

    sensoren = [t1, t2, t3, f1, f2]

    maxTemp(sensoren)



def maxTemp(sensoren):
    maxiT = max(sensor.tempWert for sensor in sensoren)
    print(f"Maximale Temperatur: {maxiT}°C")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
    finally:
        print("Hallo")



