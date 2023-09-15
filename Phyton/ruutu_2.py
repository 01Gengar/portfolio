# Print a box with input error checking

def read_input(text):
    """
    Reads user input and checks that input is valid.

    :param text: str, text that user reads on screen before inputting number
    :return: int, side of the box that is returned to main function.
    """
    side = -1
    while side <= 0:
        try:
            side = int(input(text))
        except ValueError:
            side = -1
    return side


def print_box(side_a, side_b, symbol):
    """
    Prints a box.

    :param side_a: int, Width of the box.
    :param side_b: int, Height of the box.
    :param symbol: str, Symbol, or character out of which the box is printed.
    """
    for i in range(side_b):
        print(symbol * side_a)


def main():
    width = read_input("Enter the width of a frame: ")
    height = read_input("Enter the height of a frame: ")
    mark = input("Enter a print mark: ")

    print("")
    print_box(width, height, mark)


if __name__ == "__main__":
    main()
