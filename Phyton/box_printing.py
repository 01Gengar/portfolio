# Template for task: box printing

def print_box(side_a, side_b, symbol):
    """Function for printing a box.

    :param side_a: Width of the box.
    :param side_b: Height of the box.
    :param symbol: Symbol, or character out of which the box is printed.
    """
    for i in range(side_b):
        print(symbol * side_a)


def main():
    width = int(input("Enter the width of a frame: "))
    height = int(input("Enter the height of a frame: "))
    mark = str(input("Enter a print mark: "))

    print()
    print_box(width, height, mark)


if __name__ == "__main__":
    main()
