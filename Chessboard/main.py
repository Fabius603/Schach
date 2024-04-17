from Field import Field

def main() -> None:
    field = Field()
    print(field.__repr__())
    print(field.game_field[1][1].get_moves().__repr__())

if __name__ == "__main__":
    main()