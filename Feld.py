from FigurTypen import *
from Position import Position

class Feld:
    def __init__(self) -> None:
        self.spielfeld: list[list[object]] = self.__create_spielfeld()
        self.__set_figuren("white")
        self.__set_figuren("black")
    
    def __repr__(self) -> str:
        rows: str = ""
        for figurreihe in self.spielfeld:
            row: str = ""
            for figur in figurreihe:
                row: str = row+ "|" + figur.__str__()
            row: str = row + "\n"
            rows: str = rows + row
        return rows


    def __create_spielfeld(self) -> list[list[object]]:
        spielfeld: list[list[object]] = []
        emptyField = EmptyField()
        for i in range(8):
            row: list[object] = []
            for j in range(8):
                row.append(emptyField)
            spielfeld.append(row)
        return spielfeld

    def is_move_allowed(self, position: Position, figur: object) -> bool:
        if not position.x <= 8 and not position.y <= 8:
            return False
        
        zielFeld: object = self.spielfeld[position.x][position.y]
        if isinstance(zielFeld, EmptyField):
            return False
        
        if zielFeld.color == figur.color:
            return False
        
        return True
    
    def __set_figuren(self, color: str) -> None:
        if (color == "white"):
            for i in range(8):
                pos = Position(i, 1)
                self.__set_on_field(Bauer(color, pos), pos)
        
        elif(color == "black"):
            for i in range(8):
                pos = Position(i, 6)
                self.__set_on_field(Bauer(color, pos), pos)
            
        else:
            raise Exception(f"Die Farbe {color} ist nicht vorhanden. Probiere 'white' oder 'black'")
        
    def __set_on_field(self, figur: object, position: Position) -> None:
        self.spielfeld[position.y][position.x] = figur