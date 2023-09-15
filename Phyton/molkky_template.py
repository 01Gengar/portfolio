# Code template for Mölkky.


class Player:
    """
    Class Player: implements a player plays Mölkky and
    obtains certain amount of points. The class defines
    who a player is: what information it contains and
    what operations can be carried out for it.
    """
    def __init__(self, player_name, player_points=0):
        """
        Constructor, initializes the newly created object.

        :param player_name: str, Player object
        :param player_points: int, Points player has
        """
        self.__name = player_name
        self.__points = player_points
        self.__rounds = 0
        self.__total_points = 0
        self.__success_scores = 0

    def get_name(self):
        """
        Gets name of player.

        :return: str, Name of player
        """
        return self.__name

    def get_points(self):
        """
        Gets points player currently has.

        :return: int, Player point
        """
        return self.__points

    def has_won(self):
        """
        Returns True if player has won, False otherwise.

        :return: bool, Victory status.
        """
        if self.__points == 50:
            return True
        else:
            return False

    def add_points(self, points_to_add):
        """
        Adds points to player score.

        :param points_to_add: int, Points to be added to player score.
        """
        self.__points += points_to_add
        if self.__points > 50:
            self.__points = 25
            print(self.__name, "gets penalty points!")
        elif 40 <= self.__points <= 49:
            print(self.__name, "needs only", 50 - self.__points, "points. ", end="")
            print("It's better to avoid knocking down the pins with higher points.")

    def calculate_average(self, points_to_add):
        """
        Takes in points player has gained and returns average of all points.

        :param points_to_add: int, Points to be added to total score of player.
        :return: float, Average value of scores.
        """
        self.__total_points += points_to_add
        self.__rounds += 1
        if points_to_add > 0:
            self.__success_scores += 1
        return self.__total_points / self.__rounds

    def success_percentage(self):
        """
        Calculates percentage of successful scores.

        :return: float, Percentage of successful scores.
        """
        if self.__rounds > 0:
            return (self.__success_scores / self.__rounds) * 100
        else:
            return 0.0


def main():
    # Here we define two variables which are the objects initiated from the
    # class Player. This is how the constructor of the class Player
    # (the method that is named __init__) is called!

    player1 = Player("Matti")
    player2 = Player("Teppo")

    throw = 1
    while True:

        # if throw is an even number
        if throw % 2 == 0:
            in_turn = player1

        # else throw is an odd number
        else:
            in_turn = player2

        pts = int(input("Enter the score of player " + in_turn.get_name() +
                        " of throw " + str(throw) + ": "))

        in_turn.add_points(pts)

        average = in_turn.calculate_average(pts)
        if pts > average:
            print("Cheers ", in_turn.get_name(), "!", sep="")

        if in_turn.has_won():
            print("Game over! The winner is " + in_turn.get_name() + "!")
            return

        print("")
        print("Scoreboard after throw " + str(throw) + ":")
        print(f"{player1.get_name()}: {player1.get_points()} p, hit percentage {player1.success_percentage():.1f}")
        print(f"{player2.get_name()}: {player2.get_points()} p, hit percentage {player2.success_percentage():.1f}")
        print("")

        throw += 1


if __name__ == "__main__":
    main()
