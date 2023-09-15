def main():
    continue_loop = True

    while continue_loop:
        user_input = input("Bored? (y/n) ")
        if user_input == "N" or user_input == "n":
            continue_loop
        elif user_input == "Y" or user_input == "y":
            print("Well, let's stop this, then.")
            continue_loop = False
        else:
            print("Incorrect entry.")


if __name__ == "__main__":
    main()
