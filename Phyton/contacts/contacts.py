# Program that reads contact info.


def read_file(filename):
    """
    Reads contact info from file.

    :param filename: file, File containing all contact info.
    :return: dict, All contact info as a dictionary which stores each info as iddividual dictionary.
    """
    try:
        file = open(filename, mode="r")

        name_key = {}
        keys = file.readline().strip().split(";")

        for row in file:
            values = row.strip().split(";")
            name_info_pairs = zip(keys, values)
            name_key[values[0]] = {key: value for key, value in name_info_pairs}

        file.close()

        return name_key

    except OSError:
        print("")
