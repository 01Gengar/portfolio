# Program that shows next 3 buses, based on user input of the time.

def main():
    bus_schedule = [630, 1015, 1415, 1620, 1720, 2000]
    number_of_times = len(bus_schedule)
    time = int(input("Enter the time (as an integer): "))

    for i in range(number_of_times):
        if time <= bus_schedule[i]:
            position_in_schedule = i
            break
        else:
            position_in_schedule = 0

    print("The next buses leave:")

    for i in range(3):
        if position_in_schedule == number_of_times:
            position_in_schedule = 0
        print(bus_schedule[position_in_schedule])
        position_in_schedule += 1


if __name__ == "__main__":
    main()
