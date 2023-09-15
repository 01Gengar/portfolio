# Calculate scores of participants from file game.txt


def main():
    file_name = input("Enter the name of the score file: ")

    try:
        file = open(file_name, mode="r")
    except OSError:
        print("There was an error in reading the file.")
        return

    scores = {}
    for line in file:
        line_list = line.split()
        if len(line_list) != 2:
            print("There was an erroneous line in the file:")
            print(" ".join(line_list))
            return
        elif not line_list[1].isdigit():
            print("There was an erroneous score in the file:")
            print(line_list[1])
            return

        points = int(line_list[1])
        if line_list[0] in scores:
            scores[line_list[0]] += points
        else:
            scores[line_list[0]] = points

    print("Contestant score:")
    for element in sorted(scores):
        print(element, scores[element])

    file.close()


if __name__ == "__main__":
    main()
