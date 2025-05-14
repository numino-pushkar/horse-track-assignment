class CashInventory:

    def __init__(self, inventory=None):
        self.default_stock = inventory
        self.inventory = inventory
        print(self)

    def restock(self):
        self.inventory = self.default_stock.copy()

    def add_back(self, bills: dict):
        for denom, count in bills.items():
            self.inventory[denom] += count

    def can_dispense(self, amount: int) -> bool:
        return self.dispense(amount) is not None

    def dispense(self, amount: int) -> dict | None:
        result = {}
        remaining = amount
        temp_inventory = self.inventory.copy()

        for denom in sorted(temp_inventory.keys(), reverse=True):
            count = min(remaining // denom, temp_inventory[denom])
            if count > 0:
                result[denom] = count
                remaining -= denom * count

        if remaining == 0:
            # Update real inventory
            for denom, count in result.items():
                self.inventory[denom] -= count
            return result
        else:
            return None  # Insufficient funds in required denominations

    def __str__(self):
        lines = ["Inventory:"]
        for denom in sorted(self.inventory.keys()):
            lines.append(f"${denom},{self.inventory[denom]}")
        return "\n".join(lines)
