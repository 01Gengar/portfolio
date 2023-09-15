# Program that prints result for Rubik's Cube contest.


def main():
    times = []
    for i in range(5):
        print("Enter the time for performance ", i+1, ": ", sep="", end="")
        time = float(input(""))
        times.append(time)
    sorted_times = sorted(times)
    del sorted_times[0]
    del sorted_times[-1]
    average_time = sum(sorted_times) / len(sorted_times)
    print(f"The official competition score is {average_time:.2f} seconds.")


if __name__ == "__main__":
    main()
