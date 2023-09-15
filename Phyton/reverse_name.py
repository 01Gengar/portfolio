"""
COMP.CS.100 Programming 1
Creator: Slavko Sunjic
Student id number: 151687932
Program that checks how names are inputted and makes sure that print order is first-last name.
"""


def reverse_name(inputted_name):
    """Function that receives name and checks the order,
    then returns names in right order.

    :param inputted_name: str, Name that needs checking.
    :return: str, Order is first name, last name.
    """
    if "," in inputted_name:
        names = inputted_name.split(",")
        if len(names) == 2:
            first_name = names[1].strip()
            last_name = names[0].strip()
        else:
            first_name = False
            last_name = names[0].strip()
    else:
        names = inputted_name.split()
        first_name = names[0]
        if len(names) == 2:
            last_name = names[1]
        else:
            last_name = False

    if first_name and last_name:
        name = str("".join(first_name + " " + last_name))
    elif first_name:
        name = str(first_name)
    else:
        name = str(last_name)
    return name


def main():
    name = [
            "Teddy Bear", "Bear, Teddy", "  Bear   ,    Teddy   ",
            "Teddy    Bear", "  Teddy    Bear   ", "Bear,",
            "Bear  ,", " ,   Teddy", "mr Teddy Bear", "Bear, mr Teddy",
            "Teddy von Bear", "von Bear, Teddy", "Bear,Teddy"
    ]
    for i in range(len(name)):
        print(reverse_name(name[i]), "|")


if __name__ == "__main__":
    main()
