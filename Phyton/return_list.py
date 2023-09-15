"""
Program that asks user to input how many numbers to input
and checks how many times is number from the list inputted..
"""


def input_to_list(number_of_ints):
    """Function allows user to input numbers in list and returns the list.

    :param number_of_ints: int, Defines how many numbers need to be entered.
    :return: list, List of numbers that are inputted is returned.
    """
    numbers = []
    print("Enter", number_of_ints, "numbers:")
    for i in range(number_of_ints):
        number = int(input())
        numbers.append(number)
    return numbers


def main():
    number_of_ints = int(input("How many numbers do you want to process: "))
    numbers = input_to_list(number_of_ints)
    number_to_be_searched = int(input("Enter the number to be searched: "))
    times_number_appears = numbers.count(number_to_be_searched)
    if times_number_appears > 0:
        print(number_to_be_searched, "shows up", times_number_appears, "times among the numbers you have entered.")
    else:
        print(number_to_be_searched, "is not among the numbers you have entered.")


if __name__ == "__main__":
    main()
