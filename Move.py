class Move:
    def __init__(self, x_achse: int, y_achse: int, on_first_round: bool = False) -> None:
        self.x_achse: int = x_achse
        self.y_achse: int = y_achse

    def __repr__(self) -> str:
        return f"Move(x_achse = {self.x_achse}, y_achse = {self.y_achse})"