# A program that determines user's age group (if-else and
# if-elif-else-statement).
def main():
    # Read the age as a string and convert it to an integer.
    string = input("Please, enter your age: ")
    age = int(string)
    # Print the age group, if user's age is between 0-150 years.
    if age >= 0 and age <= 150:
        # Determine the age group.
        if age == 0:
            print("You are a baby.")
        elif age < 7:
            # Age is between 1-6 years.
            print("You are a toddler.")
        elif age < 18:
            # Age is between 7-17 years.
            print("You are at school-age.")
        elif age < 40:
            # Age is between 18 and 39 years.
            print("You are a young adult.")
        elif age < 60:
            # Age is between 40-59 years.
            print("You are a middle-aged adult.")
        else:
            # The user is 60 years old or older.
            print("You are old.")
    else:
        # Print an error message.
        print("Invalid age!")


if __name__ == "__main__":
    main()
