'''
Program that simulates movements of a car across fields,
monitoring fuel consumption.
'''

import math


def menu():
    """
    This is a text-based menu.
    """
    tank_size = read_number("How much does the vehicle's gas tank hold? ")
    gas = tank_size  # Tank is full when we start
    gas_consumption = read_number("How many liters of gas does the car " +
                                  "consume per hundred kilometers? ")
    x = 0.0  # Current X coordinate of the car
    y = 0.0  # Current Y coordinate of the car

    while True:
        print("Coordinates x={:.1f}, y={:.1f}, "
              "the tank contains {:.1f} liters of gas.".format(x, y, gas))

        choice = input("1) Fill 2) Drive 3) Quit\n-> ")

        if choice == "1":
            to_fill = read_number("How many liters of gas to fill up? ")
            gas = fill(tank_size, to_fill, gas)

        elif choice == "2":
            new_x = read_number("x: ")
            new_y = read_number("y: ")
            gas, x, y = drive(x, y, new_x, new_y, gas, gas_consumption)

        elif choice == "3":
            break

    print("Thank you and bye!")


def fill(tank_size, gas_to_fill, left_gas):
    """
    This function has three parameters which are all floats:
      (1) the size of the tank
      (2) the amount of gas that is requested to be filled in
      (3) the amount of gas in the tank currently

    The parameters have to be in this order.
    The function returns one FLOAT that is the amount of gas in the
    tank AFTER the filling up.

    The function does not print anything and does not ask for any
    input.
    """
    if gas_to_fill <= tank_size - left_gas:
        new_gas = gas_to_fill + left_gas
    else:
        new_gas = tank_size

    return new_gas


def drive(x, y, dest_x, dest_y, gas, consumption):
    """
    This function has six parameters. They are all floats.
      (1) The current x coordinate
      (2) The current y coordinate
      (3) The destination x coordinate
      (4) The destination y coordinate
      (5) The amount of gas in the tank currently
      (6) The consumption of gas per 100 km of the car

    The parameters have to be in this order.
    The function returns three floats:
      (1) The amount of gas in the tank AFTER the driving
      (2) The reached (new) x coordinate
      (3) The reached (new) y coordinate

    The return values have to be in this order.
    The function does not print anything and does not ask for any
    input.
    """

    gas_left, new_x, new_y = calculate_position(gas, consumption, x, y, dest_x, dest_y)
    return gas_left, new_x, new_y


def calculate_fuel(pos_x, pos_y, dest_x, dest_y, consumption):
    """
    Calculates fuel needed to travel wanted distance.

    :param pos_x: float, Start position x of car.
    :param pos_y: float, Start position y of car.
    :param dest_x: float, End position x of car.
    :param dest_y: float, End position y of car.
    :param consumption: float, Fuel consumption of the car.
    :return: float, float, Fuel needed to travel to destination and distance to wanted destination.
    """
    travel_distance = math.sqrt((dest_x - pos_x) ** 2 + (dest_y - pos_y) ** 2)
    needed_fuel = travel_distance * consumption / 100

    return needed_fuel, travel_distance


def calculate_position(gas, consumption, pos_x, pos_y, dest_x, dest_y):
    """
    Calculates actual position where car can get with fuel it has.

    :param gas: float, Amount of fuel left in tank.
    :param consumption: float, Fuel consumption of the car.
    :param pos_x: float, Start position x of car.
    :param pos_y: float, Start position y of car.
    :param dest_x: float, End position x of car.
    :param dest_y: float, End position y of car.
    :return: float, float, float, Gas left in tank, new position of car x and y.
    """
    fuel, distance = calculate_fuel(pos_x, pos_y, dest_x, dest_y, consumption)

    if fuel <= gas:
        new_x = dest_x
        new_y = dest_y
        gas_left = gas - fuel
    else:
        actual_distance = gas * 100 / consumption
        new_x = pos_x + calculate_value(dest_x, pos_x, actual_distance, distance)
        new_y = pos_y + calculate_value(dest_y, pos_y, actual_distance, distance)
        gas_left = 0

    return gas_left, new_x, new_y


def calculate_value(x_1, x_2, p, m):
    """
    Calculate new position of car if wanted trip needs more fuel.
    :param x_1: float, Wanted destination.
    :param x_2: float, Reached destination.
    :param p: float, Trip distance.
    :param m: float, Wanted distance.
    :return: float, New position of car.
    """
    x = (x_1 - x_2) * p / m
    return x


def read_number(prompt, error_message="Incorrect input!"):
    """
    This function reads input from the user.
    """
    try:
        return float(input(prompt))

    except ValueError:
        print(error_message)
        return read_number(prompt, error_message)


def main():
    menu()


if __name__ == "__main__":
    main()
