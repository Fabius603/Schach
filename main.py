from Feld import Feld

def main() -> None:
    feld = Feld()
    print(feld.__repr__())
    print(feld.spielfeld[1][1].get_moves().__repr__())

if __name__ == "__main__":
    main()