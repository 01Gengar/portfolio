# Program that checks if values in the list are in ascending order.

def is_the_list_in_order(list):
    """Function checks if values in list are in ascending order.

    :param list: list, List with values that need to be checked.
    :return: bool, Returns True if list is in ascending order, False if not.
    """
    for i in range(1, len(list)):
        if list[i] < list[i-1]:
            return False
    return True
