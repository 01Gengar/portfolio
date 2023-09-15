# Code template for the hottest hit song Yogi Bear

def repeat_name(verse_name, number_of_repetitions=0):
    """This function prints repeating names.

    :param verse_name: Name in the song that is being repeated.
    :param number_of_repetitions: Number of line repetitions.
    :return: Returns printed text to verse function.
    """
    if number_of_repetitions:
        for i in range(number_of_repetitions):
            print(verse_name + ",", verse_name, "Bear")
    else:
        print(verse_name + ",", verse_name)


def verse(verse_words, verse_name):
    """This function forwards name in the song to repeat_words function
    and prints text of the song.

    :param verse_words: Words in the song.
    :param verse_name: Name in the song that is being forwarded for repetition.
    :return: Returns printed text to main function.
    """
    print(verse_words)
    repeat_name(verse_name)
    print(verse_words)
    repeat_name(verse_name, 3)
    print(verse_words)
    repeat_name(verse_name, 1)
    if verse_name != "Cindy":
        print("")


def main():
    verse("I know someone you don't know", "Yogi")
    verse("Yogi has a best friend too", "Boo Boo")
    verse("Yogi has a sweet girlfriend", "Cindy")


if __name__ == "__main__":
    main()
