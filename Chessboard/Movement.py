class Move:
    def __init__(self, x_achse: int, y_achse: int, on_first_round: bool = False) -> None:
        self.x_achse: int = x_achse
        self.y_achse: int = y_achse

    def __repr__(self) -> str:
        return f"Move(x_achse = {self.x_achse}, y_achse = {self.y_achse})"
    

class Direction:
    def __init__(self, *, 
                 forward: bool = False, backward: bool = False, left: bool = False, right: bool = False, \
                 leftforward: bool = False, rightforward: bool = False, leftbackward: bool = False, rightbackward: bool = False, \
                 forward_limit: int = 8, backward_limit: int = 8, left_limit: int = 8, right_limit: int = 8, \
                 leftforward_limit: int = 8, rightforward_limit: int = 8, leftbackward_limit: int = 8, rightbackward_limit: int = 8) -> None:
        
        self.forward: bool = forward
        self.backward: bool = backward
        self.left: bool = left
        self.right: bool = right
        self.leftforward: bool = leftforward
        self.rightforward: bool = rightforward
        self.leftbackward: bool = leftbackward
        self.rightbackward: bool = rightbackward

        self.forward_limit: int = forward_limit
        self.backward_limit: int = backward_limit
        self.left_limit: int = left_limit
        self.right_limit: int = right_limit
        self.leftforward_limit: int = leftforward_limit
        self.rightforward_limit: int = rightforward_limit
        self.leftbackward_limit: int = leftbackward_limit
        self.rightbackward_limit: int = rightbackward_limit

    def __repr__(self) -> str:
        return f"forward = {self.forward} limit = {self.forward_limit}, backward = {self.backward} limit = {self.backward_limit}, left = {self.left} limit = {self.left_limit}, \
        right = {self.right} limit = {self.right_limit}, leftforward = {self.leftforward} limit = {self.leftforward_limit}, \
        rightforward = {self.rightforward} limit = {self.rightforward_limit}, leftbackward = {self.leftbackward} limit = {self.leftbackward_limit}, \
        rightbackward = {self.leftbackward} limit = {self.leftbackward_limit}"