import random


class Node:
    """Ein Knoten der einfach verketteten Liste."""

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    """Einfach verkettete Liste für Ganzzahlen."""

    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, value):
        """Fügt ein Element am Ende der Liste hinzu."""
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1

    def length(self):
        """Gibt die Länge der Liste zurück."""
        return self.size

    def display(self):
        """Gibt alle Elemente der Liste aus."""
        elements = []
        current = self.head
        while current:
            elements.append(current.value)
            current = current.next
        print(" -> ".join(map(str, elements)))


# Main-Teil zum Testen der Liste
if __name__ == "__main__":
    linked_list = LinkedList()

    # Liste mit Zufallszahlen füllen
    for _ in range(10):
        linked_list.append(random.randint(1, 100))

    # Ausgabe der Länge der Liste
    print(f"Länge der Liste: {linked_list.length()}")

    # Ausgabe aller Elemente
    print("Elemente der Liste:")
    linked_list.display()
