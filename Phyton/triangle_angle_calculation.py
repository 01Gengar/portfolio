# Program that calculates angle of triangle.

def calculate_angle(angle_1, angle_2=90):
    """This function calculates unknown angle of triangle.
    
    :param angle_1: int, First known angle of triangle.
    :param angle_2: int, Second known angle of triangle.
                        If it's not inputted, than it's the right angle.
    :return: Returns the value of unknown angle.
    """
    angle_3 = 180 - angle_1 - angle_2
    return angle_3
