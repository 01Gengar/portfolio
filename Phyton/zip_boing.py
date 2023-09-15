"""
Zip-Boing Python program.

Lists all numbers, but replaces each number divisible by 3 with 'zip'
and each number divisible by 7 with 'boing'.
If number is divisible by both 3 and 7, number in list is replaced
with 'zip boing'.
"""


def main():
    user_input = int(input("How many numbers would you like to have? "))
    counter = 1

    for ind in range(0, user_input):
        if counter % 21 == 0:
            print("zip boing")
        elif counter % 7 == 0:
            print("boing")
        elif counter % 3 == 0:
            print("zip")
        else:
            print(counter)
        counter += 1


if __name__ == "__main__":
    main()
