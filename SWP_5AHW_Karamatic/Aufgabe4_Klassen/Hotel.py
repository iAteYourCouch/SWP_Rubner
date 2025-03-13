class Room():
    def __init__(self, roomType, price, availability):
        self.roomType = roomType
        self.price = price
        self.availability = availability

    def setOcc(self):
        self.availability = False

    def setFree(self):
        self.availability = True

class Hotel():
    def __init__(self, rooms=None):
        if rooms is None:
            self.rooms = []  # Falls kein Zimmer übergeben wird, leere Liste setzen
        else:
            self.rooms = rooms

    def addRoom(self, room):
        self.rooms.append(room)

def countRoomsLeft(Hotel):
    availRooms = [room for room in Hotel.rooms if room.availability]
    print(f"Verfügbare Zimmer: {len(availRooms)}")

def main():
    r1 = Room('Room 1', 100, True)
    r2 = Room('Room 2', 100, False)
    r3 = Room('Room 3', 100, True)
    r4 = Room('Room 4', 100, False)

    h1 = Hotel()
    h1.addRoom(r1)
    h1.addRoom(r2)
    h1.addRoom(r3)
    h1.addRoom(r4)
    countRoomsLeft(h1)

    r1.setOcc()

    countRoomsLeft(h1)

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
    finally:
        pass

