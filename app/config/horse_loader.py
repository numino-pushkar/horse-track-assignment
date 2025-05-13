# horse_loader.py
from app.model.horse import Horse
from app.config.config import HORSES


def load_horses_from_config() -> list[Horse]:
    return [Horse(**entry) for entry in HORSES]