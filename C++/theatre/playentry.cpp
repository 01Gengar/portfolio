/* PlayEntry class
*
* Description:
* Class file which helps in managing data.
*
* Author of the program
* Name: Slavko Sunjic
* Student number: 151687932
* Username: kdslsu
* E-Mail: slavko.sunjic@tuni.fi
*
* */

#include "playentry.hh"

PlayEntry::PlayEntry(const std::string& town, const std::string& theatre, const std::string& play, const std::string& player, int availableSeats) {
    this->town = town;
    this->theatre = theatre;
    this->play = play;
    this->player = player;
    this->availableSeats = availableSeats;
    this->alias = ""; // Set the alias to an empty string by default
}

PlayEntry::PlayEntry(const std::string& town, const std::string& theatre, const std::string& play, const std::string& alias, const std::string& player, int availableSeats) {
    this->town = town;
    this->theatre = theatre;
    this->play = play;
    this->alias = alias;
    this->player = player;
    this->availableSeats = availableSeats;
}
