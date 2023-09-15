# Program that calculates word repetition in text.


def main():
    # Test inputs:
    """user_input = [
        "I'm on a high way to hell",
        "I'm on a high way to hell",
        "It's going really well",
        "Well it's only hell",
        ""
    ]
    index = 0"""
    print("Enter rows of text for word counting. Empty row to quit.")
    list_of_words = {}
    while True:
        user_input = input("")
        # print(user_input[index])
        if user_input == "":
            break

        for word in user_input.split():
            if word.lower() in list_of_words:
                list_of_words[word.lower()] += 1
            else:
                list_of_words[word.lower()] = 1
        # index += 1

    for element in sorted(list_of_words):
        print(element, ":", list_of_words[element], "times")


if __name__ == "__main__":
    main()
