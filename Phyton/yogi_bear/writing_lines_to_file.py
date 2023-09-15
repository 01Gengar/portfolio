# Write text with numbered lines to file.


def read_message():
    """
    Reads user input and saves it to the list.

    :return: Text read from user input.
    """
    list_from_text = []

    while True:
        text_input = input("")
        if text_input == "":
            break
        else:
            list_from_text.append(text_input)

    return list_from_text


def main():
    file_name = input("Enter the name of the file: ")

    try:
        file = open(file_name, mode="w")
    except OSError:
        print(f"Writing the file {file_name} was not successful.")
        return

    print("Enter rows of text. Quit by entering an empty row.")
    file_line = read_message()

    for i in range(len(file_line)):
        print(i + 1, file_line[i], file=file)

    file.close()
    print(f"File {file_name} has been written.")


if __name__ == "__main__":
    main()
