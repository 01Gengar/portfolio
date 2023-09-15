def main():
    number_input = int(input("How many Fibonacci numbers do you want? "))
    printing_number = 1
    previous_number = 0

    for i in range(1, number_input + 1):
        next_number = printing_number + previous_number
        print(i, ". ", printing_number, sep="")
        previous_number = printing_number
        printing_number = next_number


if __name__ == "__main__":
    main()
