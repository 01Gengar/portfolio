"""
Read genres and tv-series from a file into a dict.
Print a list of the genres in alphabetical order
and list tv-series by given genre on user's command.
"""


def read_file(filename):
    """
    Reads and saves the series and their genres from the file.

    :param filename: file, File that is being processed.
    :return: dict, Data structure containing movie genres and movies.
    """

    movie_genres = {}

    try:
        file = open(filename, mode="r")

        for row in file:
            name, genres = row.rstrip().split(";")
            genres = genres.split(",")

            for genre in genres:
                if genre in movie_genres:
                    movie_genres[genre] += "," + name
                else:
                    movie_genres[genre] = name

        file.close()
        return movie_genres

    except ValueError:
        print("Error: rows were not in the format name;genres.")
        return None

    except IOError:
        print("Error: the file could not be read.")
        return None


def main():
    filename = input("Enter the name of the file: ")

    genre_data = read_file(filename)

    print("Available genres are: ", end="")
    last_genre = list(sorted(genre_data.keys()))[-1]
    for genre in sorted(genre_data):
        if genre == last_genre:
            print(genre)
        else:
            print(genre, ", ", sep="", end="")

    while True:
        genre = input("> ")

        if genre == "exit":
            return
        elif genre not in genre_data:
            continue

        movies_list = genre_data[genre].split(",")
        sorted_movies_list = sorted(movies_list)
        for i in range(len(sorted_movies_list)):
            print(sorted_movies_list[i])


if __name__ == "__main__":
    main()
