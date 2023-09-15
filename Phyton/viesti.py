def read_message():
    """
    Reads user input and saves it to the list.

    :return: Text read from user input.
    """
    # Test inputs:
    """
    message = [
        "Puff, the magic dragon lived by the sea,",
        "And frolicked in the autumn mist, in a land called Honah Lee.",
        ""
    ]
    """

    list_from_text = []
    number_of_inputs = 0
    inputs = True

    while inputs:
        text_input = input("")
        # text_input = message[number_of_inputs]
        # print(text_input)
        if text_input == "":
            inputs = False
        else:
            list_from_text.append(text_input)
            number_of_inputs += 1

    return list_from_text


def main():
    print("Enter text rows to the message. Quit by entering an empty row.")

    msg = read_message()

    print("The same, shouting:")

    for i in range(len(msg)):
        print(msg[i].upper())


if __name__ == "__main__":
    main()
