from Position import Position
from Move import Move

class EmptyField:
    def __init__(self) -> None:
        self.color: str | any = None
        self.position: str | any = None
        self.moves: str | any = None

    def __repr__(self) -> str:
        return f"EmptyField()"
    
    def __str__(self) -> str:
        return "Empty"

class Bauer:
    def __init__(self, color: str, position: Position) -> None:
        self.color: str = color
        self.position: Position = position
        self.moves: list[Move] = self.__set_moves()

    def __repr__(self) -> str:
        return f"Bauer(color = {self.color}, position = {self.position}, moves = {self.moves})"
        
    def __str__(self) -> str:
        return "Bauer"

    def __set_moves(self) -> list[Move]:
        moves: list = [
            Move(0, 1),
            Move(0, 2, True)
        ]

        if self.color == "black":
            for i in range(len(moves)):
                moves[i].y_achse = moves[i].y_achse * -1
        
        return moves
            
    def get_moves(self) -> list[Position]:
        possible_moves: list[Position] = []
        for move in self.moves:
            position = Position(self.position.x + move.x_achse, self.position.y + move.y_achse)

            possible_moves.append(position)
        return possible_moves