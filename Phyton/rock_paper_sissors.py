def main():
    # Reading the user input
    player_1 = input("Player 1, enter your choice (R/P/S): ")
    player_2 = input("Player 2, enter your choice (R/P/S): ")

    # Let's save the choices
    player_1_choice = str(player_1)
    player_2_choice = str(player_2)

    if player_1_choice == player_2_choice:
        print("It's a tie!")
    elif player_1_choice == "P" and player_2_choice == "R" or \
         player_1_choice == "R" and player_2_choice == "S" or \
         player_1_choice == "S" and player_2_choice == "P":
        print("Player 1 won!")
    else:
        print("Player 2 won!")


if __name__ == "__main__":
    main()
