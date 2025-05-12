from typing import Optional

class HorseManager:
    def __init__(self, horses: list[Horse]):
        self.horses = horses

    def get_horse(self, number: int) -> Optional[Horse]:
        return next((h for h in self.horses if h.number == number), None)

    def set_winner(self, number: int) -> bool:
        found = False
        for horse in self.horses:
            if horse.number == number:
                horse.won = True
                found = True
            else:
                horse.won = False
        return found

    def list_horses(self) -> list[str]:
        return [str(horse) for horse in self.horses]
