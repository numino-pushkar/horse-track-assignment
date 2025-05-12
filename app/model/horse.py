class Horse:
    def __init__(self, number: int, name: str, odds: int):
        self.number = number
        self.name = name
        self.odds = odds
        self.won = False

    def __str__(self):
        status = "won" if self.won else ""
        return f"{self.number} {self.name} {self.odds} {status}".strip()
