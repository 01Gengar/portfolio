# Program that asks user to input 5 numbers and prints them in reverse.

def main():
    print("Give 5 numbers:")
    numbers = []
    for i in range(5):
        number = input("Next number: ")
        numbers.append(int(number))
    print("The numbers you entered, in reverse order:")
    for i in range(4, -1, -1):
        print(numbers[i])


if __name__ == "__main__":
    main()
