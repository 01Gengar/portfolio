def count_abbas(text):
    """
    Counts abba repetition in string.

    :param text: str, Text in which it is counted.
    :return: int, Number of repetitions.
    """
    string_for_counting = "abba"
    counter = 0
    if len(text) > 3:
        for i in range(len(text)):
            if text[i:i+4] == string_for_counting:
                counter += 1

    return counter


def main():
    # Test values:
    # text = "aba"
    # text = "abba"
    # text = "abbaabba"
    text = "abbabbabba"
    # text = "abbacronymbbabba"
    # text = "antilopabbaterijabba abbaninabba"
    # text = "a b b a aba a bbabb abb ab ba abba"

    print(count_abbas(text))


if __name__ == "__main__":
    main()
