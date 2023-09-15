# Program that examines routes and distances between cities.


def find_route(data, departure, destination):
    """
    This function tries to find a route between <departure>
    and <destination> cities. It assumes the existence of
    the two functions fetch_neighbours and distance_to_neighbour
    (see the assignment and the function templates below).
    They are used to get the relevant information from the data
    structure <data> for find_route to be able to do the search.

    The return value is a list of cities one must travel through
    to get from <departure> to <destination>. If for any
    reason the route does not exist, the return value is
    an empty list [].

    :param data: dict, A dictionary which contains the distance
                       information between the cities.
    :param departure: str, the name of the departure city.
    :param destination: str, the name of the destination city.
    :return: list[str], a list of cities the route travels through, or
           an empty list if the route can not be found. If the departure
           and the destination cities are the same, the function returns
           a two element list where the departure city is stored twice.
    """
    if departure not in data:
        return []

    elif departure == destination:
        return [departure, destination]

    greens = {departure}
    deltas = {departure: 0}
    came_from = {departure: None}

    while True:
        if destination in greens:
            break

        red_neighbours = []
        for city in greens:
            for neighbour in fetch_neighbours(data, city):
                if neighbour not in greens:
                    delta = deltas[city] + distance_to_neighbour(data, city, neighbour)
                    red_neighbours.append((city, neighbour, delta))

        if not red_neighbours:
            return []

        current_city, next_city, delta = min(red_neighbours, key=lambda x: x[2])

        greens.add(next_city)
        deltas[next_city] = delta
        came_from[next_city] = current_city

    route = []
    while True:
        route.append(destination)
        if destination == departure:
            break
        destination = came_from.get(destination)

    return list(reversed(route))


def read_distance_file(file_name):
    """
    Reads the distance information from <file_name> and stores it
    in a suitable data structure (you decide what kind of data
    structure to use). This data structure is also the return value,
    unless an error happens during the file reading operation.

    :param file_name: str, The name of the file to be read.
    :return: dict | None: A dictionary containing the information
             read from the <file_name> or None if any kind of error happens.
             The data structure to be chosen is completely up to you as long
             as all the required operations can be implemented using it.
    """
    try:
        file = open(file_name, mode="r", encoding="utf-8")

        data_structure = {}
        known_cities = set()

        for line in file:
            start_city, destination_city, distance = line.strip().split(";")
            data_structure, known_cities = add_cities_to_dict(data_structure,
                                                              known_cities, start_city, destination_city, distance)

    except OSError:
        return None, None

    return data_structure, known_cities


def fetch_neighbours(data, city):
    """
    Returns a list of all the cities that are directly
    connected to parameter <city>. In other words, a list
    of cities where there exist an arrow from <city> to
    each element of the returned list. Return value is
    an empty list [], if <city> is unknown or if there are no
    arrows leaving from <city>.

    :param data: dict, A dictionary containing the distance
           information between the known cities.
    :param city: str, the name of the city whose neighbours we
           are interested in.
    :return: list[str], the neighbouring city names in a list.
             Returns [], if <city> is unknown (i.e. not stored as
             a departure city in <data>) or if there are no
             arrows leaving from the <city>.
    """
    neighbours = []

    for destination_city, distance in data.get(city, {}).items():
        neighbours.append(destination_city)

    return neighbours


def distance_to_neighbour(data, departure, destination):
    """
    Returns the distance between two neighbouring cities.
    Returns None if there is no direct connection from
    <departure> city to <destination> city. In other words
    if there is no arrow leading from <departure> city to
    <destination> city.

    :param data: dict, A dictionary containing the distance
           information between the known cities.
    :param departure: str, the name of the departure city.
    :param destination: str, the name of the destination city.
    :return: int | None, The distance between <departure> and
           <destination>. None if there is no direct connection
           between the two cities.
    """
    if departure in data and destination in data[departure]:
        return int(data[departure][destination])

    else:
        return None


def add_cities_to_dict(data_structure, known_cities, start_city,
                       destination_city, distance):
    """
    Adds starting point, destination and distance between the two.

    :param data_structure: dict, Dictionary with other departures,
                                destinations and distances.
    :param known_cities: set, Set of known cities, contains all
                              departure points and destinations.
    :param start_city: str, Departure point, or city from which
                            we are starting.
    :param destination_city: str, Destination, or city to which
                                  we want to get.
    :param distance: int, Distance between two cities.
    :return: dict, After adding new data, dictionary is returned
                    to function from which this function was called.
    """
    destination_data = {destination_city: distance}

    if start_city in data_structure:
        data_structure[start_city].update(destination_data)

    else:
        data_structure[start_city] = destination_data

    if start_city not in known_cities:
        known_cities.add(start_city)

    if destination_city not in known_cities:
        known_cities.add(destination_city)

    return data_structure, known_cities


def display_all_routes(distance_data):
    """
    Sorts all cities that are starting point alphabetically,
    then first for loop goes through all starting points and
    sorts all destinations within that starting point alphabetically.
    Sorting dictionary turns it into list, so every time function sorts
    dictionary, it has to convert it from list to dictionary.
    dict(list.items())

    :param distance_data: dict, Input from file.
    """
    sorted_by_start_city = dict(sorted(distance_data.items()))

    for start_city in sorted_by_start_city:
        sorted_by_destination = dict(sorted(sorted_by_start_city[start_city].items()))

        for destination, distance in sorted_by_destination.items():
            print(f"{start_city:<13} {destination:<13} {distance:>5}")


def input_departure(known_cities, calling_function):
    """
    Asks for input of departure point and checks if it is valid.

    :param known_cities: set, Set of known cities, contains all
                               departure points and destinations.
    :param calling_function: str, String calling function passes
                                  to check if input is valid.
                                  I used this method to identify
                                  which function is calling this function.
    :return: str, Departure point.
    """
    departure = input("Enter departure city: ")

    if calling_function == "add_city" or departure in known_cities:
        return departure

    else:
        print(f"Error: '{departure}' is unknown.")
        raise ValueError


def input_destination(data, departure, calling_function, error_input):
    """

    Asks for input of destination and checks if it is valid.

    :param data: dict, Dictionary containing all departure points,
                        destinations and distances between the two.
    :param departure: str, Departure point.
    :param calling_function: str, String calling function passes
                                  to check if input is valid.
                                  I used this method to identify which
                                  function is calling this function.
    :param error_input: str, Error message that shows if destination
                             can't be reached if action is either
                             remove, or route.
    :return: str, Destination.
    """
    destination = input("Enter destination city: ")
    list_of_cities = find_route(data, departure, destination)

    if (calling_function == "remove_city" and destination not in data[departure]
            or calling_function == "display_route" and not list_of_cities):
        print(f"{error_input} between '{departure}' and '{destination}'.")
        raise ValueError

    else:
        return destination


def add_city(data, known_cities):
    """
    Adds new departure and destination with their distance to the data.

    :param data: dict, Routes data that needs cities added to it.
    :param known_cities: set, Set of known cities, contains all
                               departure points and destinations.
    """
    departure = input_departure(known_cities, "add_city")
    destination = input_destination(data, departure, "add_city", "not_relevant")
    distance = input("Distance: ")

    if distance.isdigit():
        add_cities_to_dict(data, known_cities, departure, destination, distance)

    else:
        print(f"Error: '{distance}' is not an integer.")


def remove_city(data, known_cities):
    """
    Removes destination from departure dictionary and
    if it is only destination, removes departure as well.

    :param data: dict, Routes data that needs cities removed from it.
    :param known_cities: set, Set of known cities, contains all
                               departure points and destinations.
    """
    try:
        departure = input_departure(known_cities, "remove_city")
        destination = input_destination(data, departure,
                                        "remove_city", "Error: missing road segment")
        del data[departure][destination]

    except ValueError:
        return


def display_neighbours(data, known_cities):
    """
    Prints list of all cities connected to input city.
    Input is processed in input_check() function.

    :param data: dict, Routes data from which connecting cities are displayed.
    :param known_cities: set, Set of known cities, contains all
                               departure points and destinations.
    """
    try:
        data_structure = {}
        departure = input_departure(known_cities, "display_neighbours")

        if departure in data:

            for city in data[departure]:
                data_structure, known_cities = add_cities_to_dict(data_structure,
                                                                  known_cities, departure, city, data[departure][city])

            display_all_routes(data_structure)

    except ValueError:
        return


def display_route(data, known_cities):
    """
    Displays all cities that are connected between departure and destination input.

    :param data: dict, Routes data from which connecting cities are displayed.
    :param known_cities: set, Set of known cities, contains all
                               departure points and destinations.
    """
    try:
        departure = input_departure(known_cities, "display_route")
        destination = input_destination(data, departure, "display_route", "No route found")
        list_of_cities = find_route(data, departure, destination)
        distance = 0
        previous_city = None

        for city in list_of_cities:
            neighbour_distance = distance_to_neighbour(data, previous_city, city)
            previous_city = city

            if neighbour_distance is not None:
                distance += neighbour_distance

        print("-".join(list_of_cities), " (", distance, " km)", sep="")

    except ValueError:
        return


def main():
    input_file = input("Enter input file name: ")

    distance_data, known_cities = read_distance_file(input_file)

    if distance_data is None:
        print(f"Error: '{input_file}' can not be read.")
        return

    while True:
        action = input("Enter action> ")

        if action == "":
            print("Done and done!")
            return

        elif action == "display":
            display_all_routes(distance_data)

        elif action == "add":
            add_city(distance_data, known_cities)

        elif action == "remove":
            remove_city(distance_data, known_cities)

        elif action == "neighbours":
            display_neighbours(distance_data, known_cities)

        elif action == "route":
            display_route(distance_data, known_cities)

        else:
            print(f"Error: unknown action '{action}'.")


if __name__ == "__main__":
    main()
