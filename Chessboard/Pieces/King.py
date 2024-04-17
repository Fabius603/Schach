from Position import Position
from Movement import Move, Direction
from .SuperPiece import Piece

class King(Piece):
    def __init__(self, color: str, position: Position) -> None:
        super().__init__(color, position)

    def _set_movements(self) -> list[Move | Direction]:
        moves: list = []
        moves.append(Direction(forward=True, forward_limit=1, 
                               left=True, left_limit=1, 
                               right=True, right_limit=1,
                               backward=True, backward_limit=1, 
                               leftforward=True, leftforward_limit=1, 
                               leftbackward=True, leftbackward_limit=1, 
                               rightforward=True, rightforward_limit=1, 
                               rightbackward=True, rightbackward_limit=1))
        return moves