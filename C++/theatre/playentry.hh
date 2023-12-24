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

#ifndef PLAY_ENTRY_H
#define PLAY_ENTRY_H

#include <string>

class PlayEntry {
public:
    std::string town;
    std::string theatre;
    std::string play;
    std::string alias; // Optional, if needed
    std::string player;
    int availableSeats;

    PlayEntry(const std::string& town, const std::string& theatre, const std::string& play, const std::string& player, int availableSeats);
    PlayEntry(const std::string& town, const std::string& theatre, const std::string& play, const std::string& alias, const std::string& player, int availableSeats);
};

#endif
