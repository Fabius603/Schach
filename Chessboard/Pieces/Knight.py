from Position import Position
from Movement import Move, Direction
from .SuperPiece import Piece

class Knight(Piece):
    def __init__(self, color: str, position: Position) -> None:
        super().__init__(color, position)

    def _set_movements(self) -> list[Move | Direction]:
        moves: list = [
            Move(1, 2),
            Move(2, 1),
            Move(-2, -1),
            Move(-1, -2),
            Move(1, -2),
            Move(2, -1),
            Move(-2, 1),
            Move(-1, 2),
        ]

        return moves