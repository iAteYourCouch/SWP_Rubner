import unittest
from Poker import (
    get_card,
    count_values,
    count_suits,
    check_pair,
    check_two_pair,
    check_threekind,
    check_fourkind,
    check_flush,
    check_fullhouse,
    check_straight
)

class TestPokerFunctions(unittest.TestCase):
    def test_get_card(self):
        self.assertEqual(get_card(0), (0, 0))  # Herz Ass
        self.assertEqual(get_card(13), (1, 0))  # Karo Ass
        self.assertEqual(get_card(51), (3, 12))  # Pik König

    def test_count_values(self):
        cards = [0, 13, 26, 39, 1]  # Ass in allen Farben + 2 Herz
        self.assertEqual(count_values(cards), {0: 4, 1: 1})

    def test_count_suits(self):
        cards = [0, 13, 26, 39, 1]  # Ass in allen Farben + 2 Herz
        self.assertEqual(count_suits(cards), {0: 2, 1: 1, 2: 1, 3: 1})

    def test_check_pair(self):
        self.assertTrue(check_pair([0, 13, 26, 1, 2]))  # Ass in zwei Farben
        self.assertFalse(check_pair([0, 13, 26, 39, 1]))  # Kein Paar

    def test_check_two_pair(self):
        self.assertTrue(check_two_pair([0, 13, 1, 14, 2]))  # Zwei Paare
        self.assertFalse(check_two_pair([0, 13, 26, 39, 1]))  # Kein Zwei-Paar

    def test_check_threekind(self):
        self.assertTrue(check_threekind([0, 13, 26, 1, 2]))  # Drilling
        self.assertFalse(check_threekind([0, 13, 1, 14, 2]))  # Kein Drilling

    def test_check_fourkind(self):
        self.assertTrue(check_fourkind([0, 13, 26, 39, 1]))  # Vierling
        self.assertFalse(check_fourkind([0, 13, 26, 1, 2]))  # Kein Vierling

    def test_check_flush(self):
        self.assertTrue(check_flush([0, 1, 2, 3, 4]))  # Herz Flush
        self.assertFalse(check_flush([0, 13, 26, 39, 1]))  # Kein Flush

    def test_check_fullhouse(self):
        self.assertTrue(check_fullhouse([0, 13, 26, 1, 14]))  # Full House
        self.assertFalse(check_fullhouse([0, 13, 26, 1, 2]))  # Kein Full House

    def test_check_straight(self):
        self.assertTrue(check_straight([0, 9, 10, 11, 12]))  # Straight
        self.assertTrue(check_straight([1, 2, 3, 4, 5]))  # Straight mit niedrigem Ass
        self.assertFalse(check_straight([0, 13, 26, 39, 1]))  # Kein Straight

if __name__ == "__main__":
    unittest.main()
