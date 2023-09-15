"""
ROT13 program that encrypts words, or file. GUI has 2 fields where you can enter
your input. First field accepts any text you want to encrypt, and displays ROT13
encryption of that text in field where result is outputted. In second field, you
can enter name of file and if file with that name exists in same folder where the
main program is, new file will be created with encrypted text from original file.
I have provided 'test.txt' as file for testing purposes, but anyone can add their
own file to the folder and program will work fine. If there is any error in opening,
or reading the file, result label will show error message. Otherwise, it will
confirm successful encryption. Just remember to input exact file name with extension.
Example: 'test.txt'. If you forget '.txt', program will simply not be able to find the
file you want to convert and will output error message in result label.
"""


from tkinter import *


class Userinterface:
    def __init__(self):
        self.__main_window = Tk()  # Creation of window
        self.__main_window.title("ROT 13 encryption")  # This is title displayed on top of the window

        # Text label which instructs input of text in text box
        self.__text_label = Label(self.__main_window, height=5, width=50, text="Input regular text:")
        self.__text_label.grid(row=0, column=0, sticky=E + W)
        self.__text_entry = Text(self.__main_window, height=5, width=50, wrap=WORD)  # Text box for multi-line input
        self.__text_entry.grid(row=0, column=1, sticky=E + W)

        # Text label which instructs input of file name
        self.__file_label = Label(self.__main_window, text="Input name of the file:")
        self.__file_label.grid(row=1, column=0, sticky=E + W)
        self.__file_entry = Entry()
        self.__file_entry.grid(row=1, column=1, sticky=E + W)

        # Text label which shows the result
        self.__encrypted_label = Label(self.__main_window, height=5, width=50, text="ROT 13 encrypted text:")
        self.__encrypted_label.grid(row=2, column=0, sticky=E + W)
        self.__result_label = Label(self.__main_window, height=5, width=50, text="")
        self.__result_label.grid(row=2, column=1, sticky=E + W)

        # Button which activates encryption
        self.__encrypt_button = Button(self.__main_window, text="Encrypt text", command=self.encrypt_input,
                                       background="green", foreground="white")
        self.__encrypt_button.grid(row=3, column=0)

        # Button which closes the program
        self.__stop_button = Button(self.__main_window, text="Exit", command=self.stop,
                                    background="red", foreground="white")
        self.__stop_button.grid(row=3, column=1)

    def encrypt_input(self):
        """
        Method which calls function for encrypting the inputted text.
        It checks if we want to encrypt inputted text, or file. Converting
        both at the same time is disabled and it will just output error message.
        """
        if self.__text_entry.get("1.0", END).strip() and self.__file_entry.get().strip():
            self.__text_entry.delete("1.0", END)
            self.__file_entry.delete(0, END)
            self.__result_label.configure(text="You can't convert both at the same time \n Pick one, or the other")

        elif self.__text_entry.get("1.0", END).strip():
            text_input = self.__text_entry.get("1.0", END)
            text_output = row_encryption(text_input)
            self.__result_label.configure(text=text_output)
            self.__text_entry.delete("1.0", END)

        elif self.__file_entry.get().strip():
            file_name = self.__file_entry.get()
            text_output = read_file(file_name)
            self.__result_label.configure(text=text_output)
            self.__file_entry.delete(0, END)

    def stop(self):
        """
        Ends the execution of the program.
        """
        self.__main_window.destroy()

    def start(self):
        """
        Starts the mainloop.
        """
        self.__main_window.mainloop()


def read_file(file_name):
    """
    Reads file that user wants to encrypt.
    """
    try:
        with open(file_name, mode="r", encoding="utf-8") as file:
            list_from_text = []  # Lines of text in file will be saved to this list after encryption.
            for line in file:
                # Loop goes line by line, encrypts the line of text and saves it to the list.
                text = row_encryption(line)
                list_from_text.append(text)
        # Now to save that text into new file which will be named encrypted_ + original file name
        with open(f"encrypted_{file_name}", mode="w", encoding="utf-8") as encrypted_file:
            for line in list_from_text:
                print(line, file=encrypted_file)
        # If action was successful,confirmation message is returned to encrypt_input method
        # in Userinterface class to be outputted in result label.
        return f"'File {file_name}' successfully converted to 'encrypted_{file_name}'."
    except OSError:
        # If there is error in opening the file, error message is returned to
        # encrypt_input method in Userinterface class to be outputted in result label.
        return f"Error: File '{file_name}' can not be found!"


def read_encryption_key():
    """
    Reads original characters with their replacements from encryption.txt
    file to store them as dictionary.

    :return: dict{str: str}, Dictionary containing original
                            characters and their replacement.
    """
    with open("encryption.txt", mode="r", encoding="utf-8") as file:
        characters = {}
        for line in file:  # One line contains one character and it's encrypted counterpart
            regular_char, encrypted_char = line.split()  # We split the line into 2 characters
            characters[regular_char] = encrypted_char
            # Each character is saved as a key and encrypted counterpart as a value

    return characters


def encrypt(text):
    """
    Encrypts its parameter using ROT13 encryption technology.

    :param text: str,  string to be encrypted
    :return: str, <text> parameter encrypted using ROT13
    """
    letter = text
    characters = read_encryption_key()
    for character in characters:
        if text.lower() == character:
            if text.isupper():
                letter = characters[character].upper()
            else:
                letter = characters[character]

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
    ui = Userinterface()
    ui.start()


if __name__ == "__main__":
    main()
