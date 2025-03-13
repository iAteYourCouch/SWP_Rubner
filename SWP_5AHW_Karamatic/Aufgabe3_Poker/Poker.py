import random
from contextlib import nullcontext
from datetime import datetime
import functools

from Tools.scripts.reindent import errprint


possibilities = {
    "high_card": 0, "pair": 0, "two_pair": 0, "threekind": 0,
    "straight": 0, "flush": 0, "fullhouse": 0, "fourkind": 0,
    "straight_flush": 0, "royal_flush": 0
}


def get_card(card):
    return card // 13, card % 13


def count_values(cards):
    values = [get_card(card)[1] for card in cards]
    return {v: values.count(v) for v in set(values)}


def count_suits(cards):
    suits = [get_card(card)[0] for card in cards]
    return {s: suits.count(s) for s in set(suits)}


def check_pair(cards):
    return 2 in count_values(cards).values()


def check_two_pair(cards):
    return list(count_values(cards).values()).count(2) == 2


def check_threekind(cards):
    return 3 in count_values(cards).values()


def check_fourkind(cards):
    return 4 in count_values(cards).values()


def check_flush(cards):
    return 5 in count_suits(cards).values()


def check_fullhouse(cards):
    values = count_values(cards).values()
    return 3 in values and 2 in values


def check_straight(cards):
    values = sorted(get_card(card)[1] for card in cards)
    if values == [0, 9, 10, 11, 12]:
        return True
    return all(values[i] + 1 == values[i + 1] for i in range(4))


def draw(card_list, hand_size):
    cards = random.sample(card_list, hand_size)
    values = sorted(get_card(card)[1] for card in cards)

    if check_flush(cards):
        if values == [0, 9, 10, 11, 12]:
            possibilities["royal_flush"] += 1
        elif check_straight(cards):
            possibilities["straight_flush"] += 1
        else:
            possibilities["flush"] += 1
    elif check_straight(cards):
        possibilities["straight"] += 1
    elif check_fourkind(cards):
        possibilities["fourkind"] += 1
    elif check_fullhouse(cards):
        possibilities["fullhouse"] += 1
    elif check_threekind(cards):
        possibilities["threekind"] += 1
    elif check_two_pair(cards):
        possibilities["two_pair"] += 1
    elif check_pair(cards):
        possibilities["pair"] += 1
    else:
        possibilities["high_card"] += 1
        
        
def timer(func):
    @functools.wraps(func)
    def wrapper():
        starttime = datetime.now()
        func()
        endtime = datetime.now()
        timetaken = endtime - starttime
        print(f"\n\nAusführung des Programms dauerte {timetaken}")
    return wrapper


@timer
def main():
    cards = list(range(0, 52))
    draws = int(input("Anzahl der Ziehungen: ")) #todo input für draws, keine fixwerte(außer main)
    for _ in range(draws):
        draw(cards, 5)

    for key, value in possibilities.items():
        #ERROR: Durch null dividieren
        percent = 100 * value / draws
        print(f"{key}: {value}, {percent:.3f}%") #todo fstring


if __name__ == "__main__":
    try:
        main()

    except ZeroDivisionError:
        print("Wolltest gscheid sein, ha?")

    except ValueError:
        print("\nABC-Bär? Hallo?\n \___\n//  \\\n get stickbugged")

    except AttributeError:
        print("Wahrscheinlich irgwas mit DateTime")

    except KeyboardInterrupt:
        print("Keinen Bock mehr")

    finally:
        print("\nIch bin ein braver Schüler")


#lamda
#x = 10
#sum = lambda y: x+y
#print(sum(4))
