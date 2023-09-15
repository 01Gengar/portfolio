# Comparison of two floats

def compare_floats(float_1, float_2, EPSILON):
    """Function which compares two floating numbers.

    :param float_1: float, First number which was inputted.
    :param float_2: float, Second number which was inputted.
    :param EPSILON: float, This is acceptable rounding error.
    :return: bool, Function returns True if numbers are same and False if they are different.
    """
    if abs(float_1 - float_2) < EPSILON:
        return True
    else:
        return False


def main():
    EPSILON = 0.000000001
    float_1 = float(input("Enter first number: "))
    float_2 = float(input("Enter second number: "))
    print(compare_floats(float_1, float_2, EPSILON))


if __name__ == "__main__":
    main()
