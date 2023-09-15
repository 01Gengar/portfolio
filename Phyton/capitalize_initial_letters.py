# Program that capitalizes first letter of given words.


def capitalize_initial_letters(words):
    """Function which capitalizes first letter of each word.

    :param words: str, Words inputted by user.
    :return: str, First letter of each word is capital, rest are lower case.
    """
    word = words.title()

    return word


def main():
    # Testing phrases:
    words = "drIVING cAR"
    # words = ""
    # words = "self contained underwater breathing apparatus"
    # words = "state investigation protection agency"
    # words = "central intelligence agency"
    print(capitalize_initial_letters(words))


if __name__ == "__main__":
    main()
