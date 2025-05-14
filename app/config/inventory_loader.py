# inventory_loader.py
from app.config.config import INVENTORY


def load_inventory_from_config():
    return INVENTORY.copy()