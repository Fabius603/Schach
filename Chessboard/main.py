from Field import Field
from Position import Position

def main() -> None:
    field = Field()
    print(field.__repr__())
    print(field.get_piece_at_position(Position(1, 0)).get_moves(field))

if __name__ == "__main__":
    main()