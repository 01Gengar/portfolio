# Python program that prints dates of all fridays in 2014.

def main():

    counter = 3
    monthly_counter = 1

    for i in range(1, 13):
        if i == 2:
            number_of_days = 29
        elif i == 4 or i == 6 or i == 9 or i == 11:
            number_of_days = 31
        else:
            number_of_days = 32
        for j in range(1, number_of_days):
            if j == counter and i == monthly_counter:
                print(j, ".", i, ".", sep="")
                counter += 7
                if counter >= number_of_days:
                    new_number = counter - number_of_days + 1
                    monthly_counter += 1
                    counter = new_number


if __name__ == "__main__":
    main()
