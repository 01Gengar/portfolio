def read_message():
    """
    Reads user input and saves it to the list.

    :return: Text read from user input.
    """
    # Test inputs:
    message = [
        "CHAPTER VIII - CONCERNING THOSE WHO HAVE OBTAINED A PRINCIPALITY BY WICKEDNESS",
        "Although a prince may rise from a private station in two ways, neither of which"
        "can be entirely attributed to fortune or genius, yet it is manifest to me that I"
        "must not be silent on them, although one could be more copiously treated when I"
        "discuss republics. These methods are when, either by some wicked or nefarious ways,"
        "one ascends to the principality, or when by the favour of his fellow-citizens a"
        "private person becomes the prince of his country. And speaking of the first method,"
        "it will be illustrated by two examples--one ancient, the other modern--and without"
        "entering further into the subject, I consider these two examples will suffice those"
        "who may be compelled to follow them.",
        ""
    ]

    list_from_text = []
    # number_of_inputs = 0

    while True:
        text_input = input("")
        # text_input = message[number_of_inputs]
        # print(text_input)
        if text_input == "":
            break
        list_from_text.append(text_input)
        # number_of_inputs += 1

    return " ".join(list_from_text)


def sort_text(text, width):
    """
    Justifies the given text and prints it.

    :param text: str, Text which needs to be justified.
    :param width: int, Number of characters allocated for every line of text.
    """
    words = text.split()
    lines = []
    current_line = []

    for word in words:
        if len(' '.join(current_line + [word])) <= width:
            current_line.append(word)
        else:
            lines.append(current_line)
            current_line = [word]

    lines.append(current_line)

    output_lines = []
    for i in range(len(lines) - 1):
        line = lines[i]
        num_spaces = width - sum(len(word) for word in line)
        num_words = len(line)

        if num_words == 1:
            output_lines.append(line[0] + ' ' * num_spaces)
        else:
            space_per_gap, remainder = divmod(num_spaces, num_words - 1)
            justified_line = (' ' * (space_per_gap + 1)).join(line[:remainder + 1])
            if space_per_gap > 0:
                justified_line += ' ' * space_per_gap
            justified_line += (' ' * space_per_gap).join(line[remainder + 1:])
            output_lines.append(justified_line)

    last_line = ' '.join(lines[-1])
    print('\n'.join(output_lines))
    print(last_line)


def main():
    print("Enter text rows. Quit by entering an empty row.")

    msg = read_message()

    chars_per_line = int(input("Enter the number of characters per line: "))

    sort_text(msg, chars_per_line)


if __name__ == "__main__":
    main()
