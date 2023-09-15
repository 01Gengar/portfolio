# Trangle's Area when the Sides Are Known

from math import sqrt


def area(side_a, side_b, side_c):
    """This function calculates area of the triangle and
    returns the result to main function.

    :param side_a: First side of the triangle.
    :param side_b: Second side of the triangle.
    :param side_c: Third side of the triangle.
    :return: Area of the triangle.
    """
    s = (side_a + side_b + side_c) / 2
    area_of_triangle = sqrt(s * (s - side_a) * (s - side_b) * (s - side_c))
    return area_of_triangle


def main():
    line_a = float(input("Enter the length of the first side: "))
    line_b = float(input("Enter the length of the second side: "))
    line_c = float(input("Enter the length of the third side: "))

    print(f"The triangle's area is {area(line_a, line_b, line_c):.1f}")


if __name__ == "__main__":
    main()
