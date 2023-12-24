#include "player.hh"
#include <iostream>

// Constructor: Initialize the player with a name and zero points.
Player::Player(const std::string& name) : name_(name), points_(0) {}

// Add points to the player's score.
void Player::add_points(int points) {
    points_ += points;
    if (points_ > 50) {
        points_ = 25;
        std::cout << name_ << " gets penalty points!" << std::endl;
    }
}

// Get the player's name.
std::string Player::get_name() const {
    return name_;
}

// Get the player's total points.
int Player::get_points() const {
    return points_;
}

// Check if the player has won (reached 50 points).
bool Player::has_won() const {
    return points_ == 50;
}
