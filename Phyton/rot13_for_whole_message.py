def encrypt(text):
    """
    Encrypts its parameter using ROT13 encryption technology.

    :param text: str,  string to be encrypted
    :return: str, <text> parameter encrypted using ROT13
    """

    regular_chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                     "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
                     "w", "x", "y", "z"]

    encrypted_chars = ["n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
                       "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i",
                       "j", "k", "l", "m"]

    letter = text

    for i in range(len(regular_chars)):
        if text.lower() == regular_chars[i]:
            if text.isupper():
                letter = encrypted_chars[i].upper()
            else:
                letter = encrypted_chars[i]

    return letter


def row_encryption(text):
    """
    Sends character by character from string to encrypt() to be encrypted.

    :param text: str, string to be encrypted
    :return: str, <text> encrypted using ROT13
    """

    encrypted_text = ""

    for letter in text:
        encrypted_text += encrypt(letter)

    return encrypted_text


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

    print("ROT13:")
    for i in range(len(msg)):
        print(row_encryption(msg[i]))


if __name__ == "__main__":
    main()
