class Auto:
    """
    Eine Klasse, die ein Auto mit einer bestimmten PS-Zahl (Leistung) darstellt.
    Unterstützt Addition, Subtraktion, Multiplikation und Vergleichsoperationen.
    """

    def __init__(self, ps):
        self.ps = ps

    def __add__(self, other):
        if isinstance(other, Auto):
            return Auto(self.ps + other.ps)
        raise TypeError("Addition ist nur mit einem anderen Auto-Objekt möglich.")

    def __sub__(self, other):
        if isinstance(other, Auto):
            return Auto(self.ps - other.ps)
        raise TypeError("Subtraktion ist nur mit einem anderen Auto-Objekt möglich.")

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Auto(self.ps * other)
        raise TypeError("Multiplikation ist nur mit einer Zahl möglich.")

    def __len__(self):
        return int(self.ps)

    def __repr__(self):
        return f"Auto({self.ps} PS)"


def main():
    """
    Führt alle Methoden und Fehlerbeispiele in einem großen try-Block aus.
    """
    try:
        # Auto-Objekte erstellen
        print("\n--- Auto-Objekte erstellen ---")
        a1 = Auto(50)
        a2 = Auto(60)
        print(f"Auto 1: {a1}")
        print(f"Auto 2: {a2}")

        # Addition
        print("\n--- Addition von Autos ---")
        result_add = a1 + a2
        print(f"Ergebnis der Addition: {result_add}")

        # Subtraktion
        print("\n--- Subtraktion von Autos ---")
        result_sub = a2 - a1
        print(f"Ergebnis der Subtraktion: {result_sub}")

        # Multiplikation
        print("\n--- Multiplikation von Autos ---")
        result_mul = a1 * 2
        print(f"Ergebnis der Multiplikation: {result_mul}")

        # Länge eines Autos
        print("\n--- Länge eines Autos (PS-Wert) ---")
        print(f"Länge von Auto 1 (PS): {len(a1)}")

        # Vergleichsoperationen
        print("\n--- Vergleich von Autos ---")
        print(f"Auto 1 == Auto 2: {a1 == a2}")
        print(f"Auto 1 < Auto 2: {a1 < a2}")
        print(f"Auto 1 > Auto 2: {a1 > a2}")

        # Fehlerbeispiele
        print("\n--- Fehlerbeispiele ---")
        a_invalid = Auto(-10)  # Negativer PS-Wert
        result_add_invalid = a1 + "kein Auto"  # Ungültige Addition
        result_mul_invalid = a1 * "abc"  # Ungültige Multiplikation
        result_cmp_invalid = a1 < 10  # Vergleich mit Zahl

    except ValueError as e:
        print(f"ValueError: {e}")
    except TypeError as e:
        print(f"TypeError: {e}")
    except Exception as e:
        print(f"Unbekannter Fehler: {e}")
    finally:
        print("\n--- Abschluss ---")
        print("Das Programm wurde abgeschlossen.")


# Hauptprogramm starten
if __name__ == "__main__":
    main()
