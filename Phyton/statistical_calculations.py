# Program that calculates some statistical characteristics from user input.


import math


def average(numbers_list):
    """Function calculates average value from the provided list.

    :param numbers_list: list, List of numbers that need average calculated.
    :return: float, Returns average of the list.
    """
    # Let's calculate average value from provided list and return the result.
    # average = sum of all values from the list divided by number of the values in the list.
    average_calculated = sum(numbers_list) / len(numbers_list)
    return average_calculated


def median(numbers_list):
    """Function calculates median value from the provided list.

    :param numbers_list: list, List of numbers that need median calculated.
    :return: float, Returns median of the list.
    """
    # First, we need to sort the list in ascending order.
    # sort_nl is short for sorted_numbers_levels,
    # so calculation line of code is not too long.
    sort_nl = sorted(numbers_list)

    """
    Introduction of needed_index in if statement bellow, which represents the index number
    of value we need, either as a median, in case number of values in list is not even;
    or as value which we need to find, so we can calculate average of that value and
    first value next to it, in case number of values in the list is even.
    """
    # Let's check is number of values in the list is even, or not and do calculations based on that.
    if len(sort_nl) % 2 == 0:
        # If it's even, let's divide it by 2 and turn the result into integer.
        needed_index = int(len(sort_nl) / 2)
        # Now we have index numbers of 2 values we need to calculate the average for,
        # which is median in this case.
        median_sea_levels = average(sort_nl[(needed_index - 1):(needed_index + 1)])
    else:
        # If number of values in list is not even, when divided by 2
        # and turned into integer, it will be index number of median value.
        needed_index = int(len(sort_nl) / 2)
        median_sea_levels = sort_nl[needed_index]

    return median_sea_levels


def deviation(numbers_list):
    """Function calculates deviation value from the provided list.

    :param numbers_list: list, List of numbers that need deviation calculated.
    :return: float, Returns deviation of the list.
    """
    # This is list of values (x[i] - mean(X)) ** 2
    helper_list = []

    # Here, helper_list is filled with required values.
    for i in range(len(numbers_list)):
        helper_list.append((numbers_list[i] - average(numbers_list)) ** 2)

    # Let's calculate variance and after that,
    # calculation of list_deviation is possible
    # This could be done without variance calculation
    # as well by putting first line of calculation into
    # sqrt, but it looks more organized this way.
    variance = 1 / (len(numbers_list) - 1) * sum(helper_list)
    list_deviation = math.sqrt(variance)

    return list_deviation


def user_input():
    """Function which saves user inputs, or provided test values
    to the list sea_levels.

    :return: list, Returns list of float values to the main
                   function for further processing.
    """

    # List which is filled with user inputs.
    sea_levels = []

    # Counter for while loop which also shows index number of each input.
    number_of_inputs = 0

    # It turns to False if user input is empty string, so it stops the while loop.
    inputs = True

    while inputs:
        # Let's input all the values.
        value_input = input("")
        if value_input == "":
            # This part stops loop if input is empty string.
            inputs = False
        else:
            # Converting input to float.
            sea_level = float(value_input)

            # Adding inputs to list.
            sea_levels.append(sea_level)

            # Counting number of inputs and
            # deciding where the next input goes in list.
            number_of_inputs += 1

    return sea_levels


def main():
    print("Enter seawater levels in centimeters one per line.")
    print("End by entering an empty line.")

    # Call of function in which input of values is done
    # and they are saved to list sea_levels.
    sea_levels = user_input()

    # Output of calculated values, or error message,
    # depending on number of inputs.
    if len(sea_levels) < 2:
        print("Error: At least two measurements must be entered!")
        return
    else:
        print(f"Minimum: {min(sea_levels):8.2f} cm")
        print(f"Maximum: {max(sea_levels):8.2f} cm")
        print(f"Median: {median(sea_levels):9.2f} cm")
        print(f"Mean: {average(sea_levels):11.2f} cm")
        print(f"Deviation: {deviation(sea_levels):.2f} cm")


if __name__ == "__main__":
    main()
