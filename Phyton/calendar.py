def main():
    for i in range(1, 13):
        if i == 2:
            number_of_days = 29
        elif i == 4 or i == 6 or i == 9 or i == 11:
            number_of_days = 31
        else:
            number_of_days = 32
        for j in range(1, number_of_days):
            print(j, ".", i, ".", sep="")


if __name__ == "__main__":
    main()
