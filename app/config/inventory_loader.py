# inventory_loader.py
from app.config.config import INVENTORY


def load_inventory_from_config():
    return INVENTORY.copy()

    # for denomination, quantity in INVENTORY.items():
    #     inventory.set_bill_count(denomination, quantity)
    # return inventory