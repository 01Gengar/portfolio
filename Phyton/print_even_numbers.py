"""
Program that prints even numbers from 0 to 100
in ascending, then in descending order.
"""


def print_even_numbers(order):
    """Function that prints even numbers.

    :param order: str, Order of printing.
    """
    if order == "ascending":
        range_order = range(0, 101, 2)
    else:
        range_order = range(100, -1, -2)

    for i in range_order:
        print(i)


def main():
    print_even_numbers("ascending")
    print_even_numbers("descending")


if __name__ == "__main__":
    main()
