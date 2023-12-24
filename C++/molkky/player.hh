#ifndef PLAYER_HH
#define PLAYER_HH

#include <string>

class Player {
public:
    // Constructor: Initialize the player with a name.
    Player(const std::string& name);

    // Add points to the player's score.
    void add_points(int points);

    // Get the player's name.
    std::string get_name() const;

    // Get the player's total points.
    int get_points() const;

    // Check if the player has won (reached 50 points).
    bool has_won() const;

private:
    std::string name_;
    int points_;
};

#endif // PLAYER_HH
