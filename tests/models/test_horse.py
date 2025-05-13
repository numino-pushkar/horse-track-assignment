import unittest
from app.model.horse import Horse  # Adjust path as needed


class TestHorse(unittest.TestCase):

    def test_initialization(self):
        horse = Horse(1, "Seabiscuit", 5)
        self.assertEqual(horse.number, 1)
        self.assertEqual(horse.name, "Seabiscuit")
        self.assertEqual(horse.odds, 5)
        self.assertFalse(horse.won)

    def test_str_without_win(self):
        horse = Horse(2, "Black Beauty", 10)
        self.assertEqual(str(horse), "2 Black Beauty 10")

    def test_str_with_win(self):
        horse = Horse(3, "Secretariat", 2)
        horse.won = True
        self.assertEqual(str(horse), "3 Secretariat 2 won")

    def test_str_strip_behavior(self):
        horse = Horse(4, "Red Rum", 8)
        horse.won = False
        self.assertFalse(str(horse).endswith("won"))


if __name__ == "__main__":
    unittest.main()