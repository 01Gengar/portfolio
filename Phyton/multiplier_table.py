# Multiplier table Python program.

def main():
    user_input = int(input("Choose a number: "))
    repetition_counter = 1

    while repetition_counter <= 10:
        print(repetition_counter, "*", user_input, "=", repetition_counter * user_input)
        repetition_counter += 1


if __name__ == "__main__":
    main()
