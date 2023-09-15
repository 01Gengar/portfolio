# Program for calculating lottery victory probability.

def factoring_numbers(number_to_be_factored):
    """Function for factoring numbers.

    :param number_to_be_factored: int, Number that needs to be factored.
    :return: int, Number after factoring.
    """
    n = 1
    for i in range(1, number_to_be_factored + 1):
        n *= i
    return n


def guess_probability(all_balls, drawn_balls):
    """Function which calculates probability of winning the lottery.

    :param all_balls: Total number of balls that are in lottery.
    :param drawn_balls: Number of balls which is drawn.
    :return: Function returns probability result.
    """
    n = factoring_numbers(all_balls)  # Total number of balls in lottery for factorial calculation.
    p = factoring_numbers(drawn_balls)  # Number of drawn balls in lottery for factorial calculation.
    s = factoring_numbers(all_balls - drawn_balls)  # Number represents (n - p) for factorial calculation.
    return n / (s * p)


def main():
    all_balls = int(input("Enter the total number of lottery balls: "))
    drawn_balls = int(input("Enter the number of the drawn balls: "))
    if all_balls < 0 or drawn_balls < 0:
        print("The number of balls must be a positive number.")
    elif all_balls < drawn_balls:
        print("At most the total number of balls can be drawn.")
    else:
        lottery_probability = int(guess_probability(all_balls, drawn_balls))
        print("The probability of guessing all ", drawn_balls, " balls correctly is 1/", lottery_probability, sep="")


if __name__ == "__main__":
    main()
