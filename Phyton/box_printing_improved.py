# Improved Box Printing

def print_box(width, height, border_mark="#", inner_mark=" "):
    """Function for printing a box.

    :param width:  int, Width of the box.
    :param height: int, Height of the box.
    :param border_mark: str, Symbol, or character out of which box outline is printed.
    :param inner_mark: str, Symbol, or character out of which box is filled.
    """

    print(border_mark * width)

    for i in range(height-2):
        print(border_mark, end="")
        print(inner_mark * (width - 2), end="")
        print(border_mark)

    print(border_mark * width)


def main():
    print_box(5, 4)
    print_box(3, 8, "*")
    print_box(5, 4, "O", "o")
    print_box(inner_mark=".", border_mark="O", height=4, width=6)


if __name__ == "__main__":
    main()
