# Program that creates acronym from given words.


def create_an_acronym(words):
    """Function that creates acronym from inputted words.

    :param words: str, String of words that are inputted.
    :return: str, First letter of each word,which is also capitalized.
    """
    word = words.split()
    letters = []

    for letter in word:
        letters.append(letter[0])

    acronym = "".join(letters)
    return acronym.upper()


def main():
    # Testing phrases:
    # words = "self contained underwater breathing apparatus"
    # words = "state investigation protection agency"
    words = "central intelligence agency"
    print(create_an_acronym(words))


if __name__ == "__main__":
    main()
