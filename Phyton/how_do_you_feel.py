def main():
    # Reading the user input
    user_experience = input("How do you feel? (1-10) ")

    # Let's save the number
    saved_number = int(user_experience)

    # Check if number is correct
    if saved_number < 1 or saved_number > 10:
        print("Bad input!")
    # Printing best emoticon
    elif saved_number == 10:
        print("A suitable smiley would be :-D")
    # Printing worst emoticon
    elif saved_number == 1:
        print("A suitable smiley would be :'(")
    # Printing unsatisfied
    elif saved_number < 4:
        print("A suitable smiley would be :-(")
    # Printing neutral
    elif saved_number < 8:
        print("A suitable smiley would be :-|")
    # Printing satisfied
    else:
        print("A suitable smiley would be :-)")


if __name__ == "__main__":
    main()
