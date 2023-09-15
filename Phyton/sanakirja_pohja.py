# Code template for  tourist dictionary.


def start_up_print(dictionary_words):
    """
    Prints list of english words available in this dictionary.

    :param dictionary_words: dict, Entire dictionary structure defined in main().
    """
    print("Dictionary contents:")
    print(", ".join(sorted(dictionary_words)))


def sort_dictionary(imported_dictionary, text):
    """
    Prints entire dictionary from main().

    :param imported_dictionary: dict, Entire dictionary structure defined in main().
    :param text: str, Title of dictionary.
    """
    print(text)

    for element in sorted(imported_dictionary):
        print(element, imported_dictionary[element])

    print()


def main():
    english_spanish = {"hey": "hola", "thanks": "gracias", "home": "casa"}
    spanish_english = {"hola": "hey", "gracias": "thanks", "casa": "home"}

    start_up_print(english_spanish)
    while True:
        command = input("[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: ")

        if command == "W":
            word = input("Enter the word to be translated: ")
            if word in english_spanish:
                print(word, "in Spanish is", english_spanish[word])
            else:
                print("The word", word, "could not be found from the dictionary.")

        elif command == "A":
            en_word = input("Give the word to be added in English: ")
            sp_word = input("Give the word to be added in Spanish: ")
            english_spanish[en_word] = sp_word
            spanish_english[sp_word] = en_word
        start_up_print(english_spanish)

        elif command == "R":
            word = input("Give the word to be removed: ")
            if word in english_spanish:
                del english_spanish[word]
            else:
                print("The word", word, "could not be found from the dictionary.")

        elif command == "P":
            print()
            sort_dictionary(english_spanish, "English-Spanish")
            sort_dictionary(spanish_english, "Spanish-English")

        elif command == "T":
            sentence = input("Enter the text to be translated into Spanish: ")
            words = sentence.split()
            for i in range(len(words)):
                if words[i] in english_spanish:
                    words[i] = english_spanish[words[i]]

            print("The text, translated by the dictionary:")
            print(" ".join(words))

        elif command == "Q":
            print("Adios!")
            return

        else:
            print("Unknown command, enter W, A, R, P, T or Q!")


if __name__ == "__main__":
    main()
