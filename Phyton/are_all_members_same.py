# Program that checks if all values in list are the same, or not.

def are_all_members_same(list):
    """Function checks is all values in list are the same.

    :param list: list, List of values to be checked.
    :return: bool, Returns True if all values are the same and False if they are not.
    """
    for i in range(len(list)):
        if list[i] != list[i-1]:
            return False
    return True
