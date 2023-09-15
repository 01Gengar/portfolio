# Fractions code template


class Fraction:
    """
    This class represents one single fraction that consists of
    numerator (osoittaja) and denominator (nimittäjä).
    """
    def __init__(self, numerator, denominator):
        """
        Constructor. Checks that the numerator and denominator are of
        correct type and initializes them.

        :param numerator: int, fraction's numerator
        :param denominator: int, fraction's denominator
        """

        # isinstance is a standard function which can be used to check if
        # a value is an object of a certain class.  Remember, in Python
        # all the data types are implemented as classes.
        # ``isinstance(a, b´´) means more or less the same as ``type(a) is b´´
        # So, the following test checks that both parameters are ints as
        # they should be in a valid fraction.
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError

        # Denominator can't be zero, not in mathematics, and not here either.
        elif denominator == 0:
            raise ValueError

        self.__numerator = numerator
        self.__denominator = denominator

    def return_string(self):
        """
        :returns: str, a string-presentation of the fraction in the format
                       numerator/denominator.
        """

        if self.__numerator * self.__denominator < 0:
            sign = "-"

        else:
            sign = ""

        return f"{sign}{abs(self.__numerator)}/{abs(self.__denominator)}"

    def simplify(self):
        """
        Simplifies fractions.
        """
        gcd = greatest_common_divisor(self.__numerator, self.__denominator)
        self.__numerator //= gcd
        self.__denominator //= gcd

    def complement(self):
        """
        Forms the complement of the fraction (1 - fraction) and returns
        the result as a Fraction type object.

        :return: class, Complement of fraction
        """
        if self.__numerator < 0 or self.__denominator < 0:
            return Fraction(abs(self.__numerator), abs(self.__denominator))
        else:
            return Fraction(-self.__numerator, abs(self.__denominator))

    def reciprocal(self):
        """
        Forms the reciprocal of the fraction (1 / fraction) and returns
        the result as a Fraction type object.

        :return: class, Reciprocal of fraction
        """
        return Fraction(self.__denominator, self.__numerator)

    def multiply(self, other):
        """
        Multiplies the current fraction with another fraction.

        :param other: class, the fraction to multiply with
        :return: class, the product of the multiplication
        """
        return Fraction(self.__numerator * other.__numerator, self.__denominator * other.__denominator)

    def divide(self, other):
        """
        Divides the current fraction with another fraction.

        :param other: class, the fraction to divide with
        :return: class, the product of the dividing
        """
        return Fraction(self.__numerator * other.__denominator, self.__denominator * other.__numerator)

    def add(self, other):
        """
        Calculates sum of 2 fractions.

        :param other: class, the fraction we add to self fraction
        :return: class, sum of 2 fractions
        """
        new_numerator_1 = self.__numerator * other.__denominator
        new_numerator_2 = other.__numerator * self.__denominator
        new_denominator = self.__denominator * other.__denominator
        return Fraction(new_numerator_1 + new_numerator_2, new_denominator)

    def deduct(self, other):
        """
        Calculates difference of 2 fractions.

        :param other: class, the fraction we deduct from self fraction
        :return: class, difference between 2 fractions
        """
        new_numerator_1 = self.__numerator * other.__denominator
        new_numerator_2 = other.__numerator * self.__denominator
        new_denominator = self.__denominator * other.__denominator
        return Fraction(new_numerator_1 - new_numerator_2, new_denominator)

    def __lt__(self, other):
        """
        Less than comparison implementation

        :param other: class, the fraction we are comparing to
        :return bool, True if other fraction is less
        """
        return self.__numerator * other.__denominator < self.__denominator * other.__numerator

    def __gt__(self, other):
        """
        Greater than comparison implementation

        :param other: class, the fraction we are comparing to
        :return bool, True if other fraction is greater
        """
        return self.__numerator * other.__denominator > self.__denominator * other.__numerator

    def __str__(self):
        """
        Prints fraction.

        :return: str, a string-presentation of the fraction in the format
                       numerator/denominator.
        """

        if self.__numerator * self.__denominator < 0:
            sign = "-"

        else:
            sign = ""

        return f"{sign}{abs(self.__numerator)}/{abs(self.__denominator)}"


def greatest_common_divisor(a, b):
    """
    Euclidean algorithm. Returns the greatest common
    divisor (suurin yhteinen tekijä).  When both the numerator
    and the denominator is divided by their greatest common divisor,
    the result will be the most reduced version of the fraction in question.
    """
    while b != 0:
        a, b = b, a % b

    return a


def main():
    fractions = {}
    while True:
        command = input("> ")
        if command == "quit":
            print("Bye bye!")
            break

        elif command == "add":
            fraction_str = input("Enter a fraction in the form integer/integer: ")
            fraction_name = input("Enter a name: ")
            numerator, denominator = map(int, fraction_str.split("/"))
            fraction = Fraction(numerator, denominator)
            fractions[fraction_name] = fraction

        elif command == "print":
            print_name = input("Enter a name: ")
            if print_name in fractions:
                print(f"{print_name} = {fractions[print_name].return_string()}")
            else:
                print(f"Name {print_name} was not found")

        elif command == "list":
            for name in sorted(fractions):
                print(f"{name} = {fractions[name].return_string()}")

        elif command == "*":
            operand_1 = input("1st operand: ")
            if operand_1 in fractions:
                operand_2 = input("2nd operand: ")
                if operand_2 in fractions:
                    frac_1 = fractions[operand_1].return_string()
                    frac_2 = fractions[operand_2].return_string()
                    frac_multiplied = fractions[operand_1].multiply(fractions[operand_2])
                    print(f"{frac_1} * {frac_2} = {frac_multiplied}")
                    frac_multiplied.simplify()
                    print(f"simplified {frac_multiplied.return_string()}")
                else:
                    print(f"Name {operand_2} was not found")
            else:
                print(f"Name {operand_1} was not found")

        elif command == "file":
            file_name = input("Enter the name of the file: ")
            try:
                file = open(file_name, mode="r")
                for line in file:
                    parts = line.split("=")
                    if len(parts) != 2:
                        raise OSError
                    else:
                        fract_name, file_fraction = parts
                    fraction_parts = file_fraction.split("/")
                    if len(fraction_parts) != 2:
                        raise OSError
                    file_num, file_den = map(int, fraction_parts)
                    fraction = Fraction(file_num, file_den)
                    fractions[fract_name] = fraction

                file.close()

            except OSError:
                print("Error: the file cannot be read.")

        else:
            print("Unknown command!")


if __name__ == "__main__":
    main()
