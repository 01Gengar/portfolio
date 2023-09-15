# ROT13 program code template


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


def main():
    # Testing phrases:
    words = "abc efg Hij klM nop RST uvz ?!0 123"
    # words = "drIVING cAR"
    # words = ""
    # words = "?"
    # words = "self contained underwater breathing apparatus"
    # words = "state investigation protection agency"
    # words = "central intelligence agency"

    # letter = input("")
    print(words)
    print(row_encryption(words))


if __name__ == "__main__":
    main()
