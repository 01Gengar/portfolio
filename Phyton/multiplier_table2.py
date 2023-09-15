# Second version of multiplier table Python program.

def main():
    user_input = int(input("Choose a number: "))
    multiplier = 1
    answer = int()

    while answer <= 100:
        answer = multiplier * user_input
        print(multiplier, "*", user_input, "=", answer)
        multiplier += 1


if __name__ == "__main__":
    main()
