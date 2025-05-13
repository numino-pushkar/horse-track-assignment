import unittest
from app.model.cash_inventory import CashInventory  # Adjust path as needed


class TestCashInventory(unittest.TestCase):

    def setUp(self):
        self.initial_inventory = {100: 2, 20: 3, 10: 5, 5: 5, 1: 10}
        self.inventory = CashInventory(inventory=self.initial_inventory.copy())

    def test_initial_inventory(self):
        self.assertEqual(self.inventory.inventory, self.initial_inventory)

    def test_restock(self):
        self.inventory.dispense(135)  # Use some bills
        self.inventory.restock()
        self.assertEqual(self.inventory.inventory, self.initial_inventory)

    def test_add_back(self):
        bills = {20: 1, 1: 4}
        self.inventory.add_back(bills)
        expected = self.initial_inventory.copy()
        expected[20] += 1
        expected[1] += 4
        self.assertEqual(self.inventory.inventory, expected)

    def test_can_dispense_true(self):
        self.assertTrue(self.inventory.can_dispense(85))  # Should be dispensable

    def test_can_dispense_false(self):
        self.assertFalse(self.inventory.can_dispense(999))  # Too high to dispense

    def test_dispense_success(self):
        result = self.inventory.dispense(130)
        self.assertIsNotNone(result)
        self.assertEqual(sum(k * v for k, v in result.items()), 130)

        # Inventory should now be reduced correctly
        total_used = sum(result[k] for k in result)
        self.assertLess(total_used, sum(self.initial_inventory.values()))

    def test_dispense_failure(self):
        result = self.inventory.dispense(999)  # Not possible with given stock
        self.assertIsNone(result)

    def test_str_representation(self):
        inventory_str = str(self.inventory)
        self.assertIn("Inventory:", inventory_str)
        self.assertIn("$100,2", inventory_str)
        self.assertIn("$1,10", inventory_str)


if __name__ == '__main__':
    unittest.main()
