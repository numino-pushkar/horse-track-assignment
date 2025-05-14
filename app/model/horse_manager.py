from typing import Optional
from app.model.horse import Horse


class HorseManager:
    def __init__(self, horses: list[Horse]):
        self.horses = horses

    def get_horse(self, number: int) -> Optional[Horse]:
        return next((h for h in self.horses if h.number == number), None)

    def set_winner(self, number: int) -> bool:
        if not self.is_valid_horse(number):
            return False
        for horse in self.horses:
            horse.won = horse.number == number
        return True

    def list_horses(self) -> list[str]:
        return [str(horse) for horse in self.horses]

    def is_valid_horse(self, horse_number: int) -> bool:
        return any(horse.number == horse_number for horse in self.horses)

    def __str__(self) -> str:
        return "Horses:\n" + "\n".join(
            f"{horse.number},{horse.name},{horse.odds},{horse.won}" for horse in self.horses
        )
