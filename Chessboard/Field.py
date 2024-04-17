from Pieces import Piece, EmptyField, Pawn, Rook, Knight, Bishop, Queen, King
from Position import Position

class Field:
    def __init__(self) -> None:
        self.game_field: list[list[Piece]] = self.__create_game_field()
        self.__set_pieces("white")
        self.__set_pieces("black")
    
    def __repr__(self) -> str:
        rows: str = ""
        for piece_rows in self.game_field:
            row: str = ""
            for piece in piece_rows:
                row: str = row+ "|" + piece.__str__()
            row: str = row + "\n"
            rows: str = rows + row
        return rows


    def __create_game_field(self) -> list[list[Piece]]:
        game_field: list[list[Piece]] = []
        emptyField = EmptyField()
        for _ in range(8):
            row: list[Piece] = []
            for _ in range(8):
                row.append(emptyField)
            game_field.append(row)
        return game_field

    def is_move_allowed(self, position: Position, piece: Piece) -> bool:
        if not position.x <= 8 and not position.y <= 8:
            return False
        
        zielFeld: Piece = self.game_field[position.x][position.y]
        if isinstance(zielFeld, EmptyField):
            return False
        
        if zielFeld.color == piece.color:
            return False
        
        return True
    
    def __set_pieces(self, color: str) -> None:
        if (color == "white"):
            for i in range(8):
                pos = Position(i, 1)
                self.__set_on_field(Pawn(color, pos), pos)
        
        elif(color == "black"):
            for i in range(8):
                pos = Position(i, 6)
                self.__set_on_field(Pawn(color, pos), pos)
            
        else:
            raise Exception(f"Die Farbe {color} ist nicht vorhanden. Probiere 'white' oder 'black'")
        
    def __set_on_field(self, piece: Piece, position: Position) -> None:
        if self.is_move_allowed(position, piece):
            self.game_field[position.y][position.x] = piece
            return

        raise Exception("Position is outside of chessboard")