# Code for returning longest alphabetically ordered substring.


def longest_substring_in_order(text):
    """
    Finds longest alphabetically ordered substring.

    :param text: str, String from which substring is looked for.
    :return: str, Longest alphabetically ordered substring.
    """
    substring = ""
    temp_substring = ""

    for i in range(len(text)):
        if i == 0 or text[i] > text[i-1]:
            temp_substring += text[i]
        else:
            if len(temp_substring) > len(substring):
                substring = temp_substring

            temp_substring = text[i]

    if len(temp_substring) > len(substring):
        substring = temp_substring

    return substring


def main():
    # Test values:
    # text = "abcedabcdefg"
    # text = "abcabcdefgabab"
    text = "acdkbarstyefgioprtyrtyx"
    # text = ""
    # text = "aba"
    # text = "abba"
    # text = "abbaabba"
    # text = "abbabbabba"
    # text = "abbacronymbbabba"
    # text = "antilopabbaterijabba abbaninabba"
    # text = "a b b a aba a bbabb abb ab ba abba"

    print(longest_substring_in_order(text))


if __name__ == "__main__":
    main()
