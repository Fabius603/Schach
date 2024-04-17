from .SuperPiece import Piece
from Movement import Move, Direction

class EmptyField(Piece):
    def __init__(self, color=None, position=None) -> None:
        super().__init__(color, position)

    def __repr__(self) -> str:
        return f"EmptyField()"
    
    def __str__(self) -> str:
        return "Empty"
    
    def _set_movements(self) -> list[Move | Direction]:
        return []
    
    def get_moves(self) -> list[Move]:
        return []