# Code template for geometric patterns.

import math


def print_circumference(circumference):
    """Function that prints circumference value.

    :param circumference: float, Circumference of object calculated
                                in calculate_circumference function.
    """
    print(f"The circumference is {circumference:.2f}")


def print_area(area):
    """Function that prints circumference value.

    :param area: float, Area of object calculated
                        in calculate_area function.
    """
    print(f"The surface area is {area:.2f}")


def calculate_circumference(side_1, side_2):
    """Function that calculates circumference of object.

    :param side_1: float, Side of square, or first side of rectangle.
    :param side_2: float, If it is square, this parameter does not exists,
                            or it is second side of rectangle.
    """
    circumference = 2 * (side_1 + side_2)
    print_circumference(circumference)


def calculate_area(side_1, side_2):
    """Function that calculates surface area of object.

    :param side_1: float, Side of square, or first side of rectangle, or pi value for circle.
    :param side_2: float, If it is square, this parameter is same a side_1,
                            or it is second side of rectangle, or radius^2 of circle.
    """
    area = side_1 * side_2
    print_area(area)


def input_square():
    """
    Print a promt that asks dimensions of a square side.
    """
    square_side = 0

    while square_side <= 0:
        square_side = float(input("Enter the length of the square's side: "))

    calculate_circumference(square_side, square_side)
    calculate_area(square_side, square_side)


def input_rectangle():
    """
    Print a promt that asks dimensions of a rectangle sides.
    """
    rectangle_side_1 = 0
    rectangle_side_2 = 0

    while rectangle_side_1 <= 0:
        rectangle_side_1 = float(input("Enter the length of the rectangle's side 1: "))

    while rectangle_side_2 <= 0:
        rectangle_side_2 = float(input("Enter the length of the rectangle's side 2: "))

    calculate_circumference(rectangle_side_1, rectangle_side_2)
    calculate_area(rectangle_side_1, rectangle_side_2)


def input_circle():
    """
    Print a promt that asks dimensions of a circle radius.
    """
    circle_radius = 0

    while circle_radius <= 0:
        circle_radius = float(input("Enter the circle's radius: "))

    calculate_circumference(math.pi * circle_radius, 0)
    calculate_area(math.pi, circle_radius * circle_radius)


def menu():
    """
    Print a menu for user to select which geometric pattern to use in calculations.
    """
    while True:
        answer = input("Enter the pattern's first letter or (q)uit: ")

        if answer == "s":
            input_square()

        elif answer == "r":
            input_rectangle()

        elif answer == "c":
            input_circle()

        elif answer == "q":
            return

        else:
            print("Incorrect entry, try again!")

        # Empty row for the sake of readability.
        print()


def main():
    menu()
    print("Goodbye!")


if __name__ == "__main__":
    main()
