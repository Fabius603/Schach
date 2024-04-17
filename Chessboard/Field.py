from Pieces import Piece, EmptyField
from Position import Position

class Field:
    def __init__(self) -> None:
        self.game_field: list[list[Piece]] = self.__create_game_field()
        self.__set_pieces_on_start("white")
        self.__set_pieces_on_start("black")
    
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

    def is_move_allowed(self, target_position: Position, piece: Piece) -> bool:
        if 0 > target_position.x < 7 or 0 > target_position.y < 7:
            return False
        
        target_field: Piece = self.get_piece_at_position(target_position)
        
        if isinstance(target_field, EmptyField):
            return True
        
        if target_field.color == piece.color:
            return False

        # An dieser Stelle ist klar, dass eine gegnerische Figur angreifbar ist        
        return True
    
    def __set_pieces_on_start(self, color: str) -> None:
        from Pieces import Pawn, Rook, Knight, Bishop, Queen, King

        if (color == "white"):
            for i in range(8):
                self.__set_on_field(Pawn(color, Position(i, 6)), Position(i, 6))
            self.__set_on_field(Rook(color, Position(0, 7)), Position(0, 7))
            self.__set_on_field(Knight(color, Position(1, 7)), Position(1, 7))
            self.__set_on_field(Bishop(color, Position(2, 7)), Position(2, 7))
            self.__set_on_field(Queen(color, Position(3, 7)), Position(3, 7))
            self.__set_on_field(King(color, Position(4, 7)), Position(4, 7))
            self.__set_on_field(Bishop(color, Position(5, 7)), Position(5, 7))
            self.__set_on_field(Knight(color, Position(6, 7)), Position(6, 7))
            self.__set_on_field(Rook(color, Position(7, 7)), Position(7, 7))
        
        elif(color == "black"):
            for i in range(8):
                pos = Position(i, 1)
                self.__set_on_field(Pawn(color, pos), pos)
            self.__set_on_field(Rook(color, Position(0, 0)), Position(0, 0))
            self.__set_on_field(Knight(color, Position(1, 0)), Position(1, 0))
            self.__set_on_field(Bishop(color, Position(2, 0)), Position(2, 0))
            self.__set_on_field(Queen(color, Position(3, 0)), Position(3, 0))
            self.__set_on_field(King(color, Position(4, 0)), Position(4, 0))
            self.__set_on_field(Bishop(color, Position(5, 0)), Position(5, 0))
            self.__set_on_field(Knight(color, Position(6, 0)), Position(6, 0))
            self.__set_on_field(Rook(color, Position(7, 0)), Position(7, 0))

        else:
            raise Exception(f"Die Farbe {color} ist nicht vorhanden. Probiere 'white' oder 'black'")
        
    def __set_on_field(self, piece: Piece, target_position: Position) -> None:
        self.game_field[target_position.y][target_position.x] = piece
        piece.position = target_position
            

    def get_piece_at_position(self, position: Position) -> Piece:
        return self.game_field[position.y][position.x]
    
    def move_piece_to_position(self, piece: Piece, target_position: Position) -> None:
        if self.is_move_allowed(target_position, piece):
            self.__set_on_field(piece, target_position)
            self.__set_on_field(EmptyField(), piece.position)  
