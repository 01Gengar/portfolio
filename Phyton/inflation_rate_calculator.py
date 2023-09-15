# Program for inflation rate calculation

def main():

    loop_breaker = True
    number_of_month = 1
    inflation = []

    while loop_breaker:
        print("Enter inflation rate for month ", number_of_month, ": ", sep="", end="")
        inflation_input = input("")
        if inflation_input == "" and number_of_month >= 3:
            loop_breaker = False
        elif inflation_input == "" and number_of_month < 3:
            print("Error: at least 2 monthly inflation rates must be entered.")
            return
        else:
            inflation.append(float(inflation_input))
            number_of_month += 1

    max_inflation = -1000.0

    for i in range(len(inflation) - 1):
        inflation_difference = inflation[i + 1] - inflation[i]
        if inflation_difference > max_inflation:
            max_inflation = inflation_difference

    print(f"Maximum inflation rate change was {max_inflation:.1f} points.")


if __name__ == "__main__":
    main()
