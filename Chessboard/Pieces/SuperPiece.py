from Position import Position
from Move import Move
from abc import ABC, abstractmethod

class Piece(ABC):
    def __init__(self, color, position) -> None:
        self.color: str = color
        self.position: str = position
        self.moves: list[Move] = self._set_moves()

    @abstractmethod
    def __repr__(self) -> str:
        return "__repr__ Methode muss noch eingerichtet werden!"
    
    @abstractmethod
    def __str__(self) -> str:
        return "__str__ Methode muss noch eingerichtet werden!"

    @abstractmethod
    def _set_moves(self) -> list[Move]:
        return []
    
    @abstractmethod
    def get_moves() -> list[Move]:
        return []
    

class Pawn(Piece):
    def __init__(self, color: str, position: Position) -> None:
        super().__init__(color, position)

    def __repr__(self) -> str:
        return f"Pawn(color = {self.color}, position = {self.position}, moves = {self.moves})"
        
    def __str__(self) -> str:
        return "Pawn"

    def _set_moves(self) -> list[Move]:
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