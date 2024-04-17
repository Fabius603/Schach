from Position import Position
from Movement import Move, Direction
from abc import ABC, abstractmethod

class Piece(ABC):
    def __init__(self, color, position) -> None:
        self.color: str = color
        self.position: Position = position
        self.moves: list[Move | Direction] = self._set_movements()

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(color = {self.color}, position = {self.position}, moves = {self.moves})"
        
    def __str__(self) -> str:
        return self.__class__.__name__

    @abstractmethod
    def _set_movements(self) -> list[Move | Direction]:
        return []

    def get_moves(self, field) -> list[Position]:
        from Field import Field
        possible_moves: list[Position] = []
        for move in self.moves:
            if isinstance(move, Move):
                target_position: Position = Position(self.position.x + move.x_achse, self.position.y + move.y_achse)
                if field.is_move_allowed(target_position, self):
                    possible_moves.append(target_position)

            elif isinstance(move, Direction):
                if move.forward:
                    for i in range(move.forward_limit):
                        if(self.color == "white"):
                            target_position: Position = Position(self.position.x, self.position.y + i + 1)
                        else:
                            target_position: Position = Position(self.position.x, self.position.y - i + 1)

                        if field.is_move_allowed(target_position, self):
                            possible_moves.append(target_position)
                        else:
                            break
                
                if move.backward:
                    for i in range(move.backward_limit):
                        if(self.color == "white"):
                            target_position: Position = Position(self.position.x, self.position.y - i + 1)
                        else:
                            target_position: Position = Position(self.position.x, self.position.y + i + 1)

                        if field.is_move_allowed(target_position, self):
                            possible_moves.append(target_position)
                        else:
                            break

                if move.left:
                    for i in range(move.left_limit):
                        if(self.color == "white"):
                            target_position: Position = Position(self.position.x - i + 1, self.position.y)
                        else:
                            target_position: Position = Position(self.position.x + i + 1, self.position.y)

                        if field.is_move_allowed(target_position, self):
                            possible_moves.append(target_position)
                        else:
                            break

                if move.right:
                    for i in range(move.right_limit):
                        if(self.color == "white"):
                            target_position: Position = Position(self.position.x + i + 1, self.position.y)
                        else:
                            target_position: Position = Position(self.position.x - i + 1, self.position.y)

                        if field.is_move_allowed(target_position, self):
                            possible_moves.append(target_position)
                        else:
                            break

                if move.leftforward:
                    for i in range(move.leftforward_limit):
                        if(self.color == "white"):
                            target_position: Position = Position(self.position.x + i + 1, self.position.y + i + 1)
                        else:
                            target_position: Position = Position(self.position.x - i + 1, self.position.y - i + 1)

                        if field.is_move_allowed(target_position, self):
                            possible_moves.append(target_position)
                        else:
                            break

                if move.rightforward:
                    for i in range(move.rightforward_limit):
                        if(self.color == "white"):
                            target_position: Position = Position(self.position.x - i + 1, self.position.y + i + 1)
                        else:
                            target_position: Position = Position(self.position.x + i + 1, self.position.y - i + 1)

                        if field.is_move_allowed(target_position, self):
                            possible_moves.append(target_position)
                        else:
                            break
                
                if move.rightbackward:
                    for i in range(move.rightbackward_limit):
                        if(self.color == "white"):
                            target_position: Position = Position(self.position.x - i + 1, self.position.y - i + 1)
                        else:
                            target_position: Position = Position(self.position.x + i + 1, self.position.y + i + 1)

                        if field.is_move_allowed(target_position, self):
                            possible_moves.append(target_position)
                        else:
                            break

                if move.leftbackward:
                    for i in range(move.leftbackward_limit):
                        if(self.color == "white"):
                            target_position: Position = Position(self.position.x + i + 1, self.position.y - i + 1)
                        else:
                            target_position: Position = Position(self.position.x - i + 1, self.position.y + i + 1)

                        if field.is_move_allowed(target_position, self):
                            possible_moves.append(target_position)
                        else:
                            break

        return possible_moves