from Position import Position
from Movement import Move, Direction
from .SuperPiece import Piece

class Queen(Piece):
    def __init__(self, color: str, position: Position) -> None:
        super().__init__(color, position)

    def _set_movements(self) -> list[Move | Direction]:
        moves: list = []
        moves.append(Direction(forward=True, left=True, right=True, backward=True, leftforward=True, leftbackward=True, rightforward=True, rightbackward=True))
        return moves