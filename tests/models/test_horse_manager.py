import unittest
from app.model.horse import Horse
from app.model.horse_manager import HorseManager


class TestHorseManager(unittest.TestCase):

    def setUp(self):
        self.horses = [
            Horse(1, "Seabiscuit", 5),
            Horse(2, "Secretariat", 3),
            Horse(3, "Black Beauty", 10)
        ]
        self.manager = HorseManager(self.horses)

    def test_get_horse_found(self):
        horse = self.manager.get_horse(2)
        self.assertIsNotNone(horse)
        self.assertEqual(horse.name, "Secretariat")

    def test_get_horse_not_found(self):
        horse = self.manager.get_horse(99)
        self.assertIsNone(horse)

    def test_set_winner_valid(self):
        result = self.manager.set_winner(3)
        self.assertTrue(result)
        for horse in self.horses:
            if horse.number == 3:
                self.assertTrue(horse.won)
            else:
                self.assertFalse(horse.won)

    def test_set_winner_invalid(self):
        result = self.manager.set_winner(99)
        self.assertFalse(result)
        self.assertTrue(all(not horse.won for horse in self.horses))


if __name__ == "__main__":
    unittest.main()
