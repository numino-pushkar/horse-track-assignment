class CashInventory:

    def __init__(self, inventory=None):
        self.default_stock = inventory.copy()
        self.inventory = inventory.copy()

    def restock(self):
        self.inventory = self.default_stock.copy()

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
