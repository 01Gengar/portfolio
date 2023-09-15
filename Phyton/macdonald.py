# Template Song: Old MacDonald

def print_verse(animal, vocalization):
    """This function, when called, outputs text of Old MacDonald song

    There are two parameters that are inputted from main function.
    :param animal: str, the name of the animal.
    :param vocalization: str, the sound animal is making.
    """
    print("Old MACDONALD had a farm")
    print("E-I-E-I-O")
    print("And on his farm he had a", animal)
    print("E-I-E-I-O")
    print("With a", vocalization, vocalization, "here")
    print("And a", vocalization, vocalization, "there")
    print("Here a", vocalization + ",", "there a", vocalization)
    print("Everywhere a", vocalization, vocalization)
    print("Old MacDonald had a farm")
    print("E-I-E-I-O")


def main():
    print_verse("cow", "moo")
    print("")
    print_verse("pig", "oink")
    print("")
    print_verse("duck", "quack")
    print("")
    print_verse("horse", "neigh")
    print("")
    print_verse("lamb", "baa")


if __name__ == "__main__":
    main()
