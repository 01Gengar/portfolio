/* Theatre play data
*
* Description:
* Program reads theatre play data from different theaters
* provided in file that is read on program startup.
*
* Commands to use are:
* - quit - The program quits
* - theatres - Prints all the known theatres in alphabetical order
* - plays - Prints all the plays in alphabetical order
* - theatres_of_play <play> - Prints all the theatres
* that offer the given play in alphabetical order
* - plays_in_theatre <theatre> - Prints the plays
* of the given theatre in alphabetical order
* - plays_in_town <town> - Prints those plays in the given town
* that has free seats
* - players_in_play <play> [<theatre>] - Prints players in
* the given play. There can be identical plays in different theatres,
* and thus, the command allows theatre name as an optional parameter
*
* Author of the program
* Name: Slavko Sunjic
* Student number: 151687932
* Username: kdslsu
* E-Mail: slavko.sunjic@tuni.fi
*
* Notes on the program and its implementation (if there are):
*
* */

#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <cstdlib>
#include <algorithm>
#include <sstream>
#include <map>
#include <set>
#include "playentry.hh"

using namespace std;

// Fields in the input file
const int NUMBER_OF_FIELDS = 5;

// Command prompt
const string PROMPT = "the> ";

// Error and other messages
const string EMPTY_FIELD = "Error: empty field in line ";
const string FILE_ERROR = "Error: input file cannot be opened";
const string WRONG_PARAMETERS = "Error: wrong number of parameters";
const string THEATRE_NOT_FOUND = "Error: unknown theatre";
const string PLAY_NOT_FOUND = "Error: unknown play";
const string PLAYER_NOT_FOUND = "Error: unknown player";
const string TOWN_NOT_FOUND = "Error: unknown town";
const string COMMAND_NOT_FOUND = "Error: unknown command";
const string NOT_AVAILABLE = "No plays available";

// Casual split function, if delim char is between "'s, ignores it.
vector<string> split(const string& str, char delim) {
    vector<string> result = {""};
    bool inside_quotation = false;
    for (char current_char : str) {
        if (current_char == '"') {
            inside_quotation = not inside_quotation;
        } else if (current_char == delim and not inside_quotation) {
            result.push_back("");
        } else {
            result.back().push_back(current_char);
        }
    }
    return result;
}

// Function to check if a string is a positive integer or "none"
bool isPositiveIntegerOrNone(const string& str) {
    if (str == "none") {
        return true;
    }
    for (char c : str) {
        if (!isdigit(c)) {
            return false;
        }
    }
    return true;
}

// Function to read a file, or to terminate  a program in case of error
vector<PlayEntry> readFile(const string& filename) {
    ifstream input_file(filename);

    // Checks if file with provided name exists
    // If not, program is terminated with EXIT_FAILURE
    if (!input_file.is_open()) {
        cout << FILE_ERROR << endl;
        exit(EXIT_FAILURE);
    }

    vector<PlayEntry> playEntries; // For storing data from file into class

    string line;
    int line_number = 0;

    while (getline(input_file, line)) {
        line_number++; // Goes trough file line by line
        vector<string> fields = split(line, ';');

        // Checks if each line contains required number of fields
        // If not, program is terminated with EXIT_FAILURE
        if (fields.size() != NUMBER_OF_FIELDS) {
            cout << EMPTY_FIELD << line_number << endl;
            exit(EXIT_FAILURE);
        }

        // Fields in the file
        string town = fields[0];
        string theatre = fields[1];
        string play = fields[2];
        string player = fields[3];
        string seats_str = fields[4];

        // Checks if seats field contains required data
        // If not, program is terminated with EXIT_FAILURE
        if (!isPositiveIntegerOrNone(seats_str)) {
            cout << EMPTY_FIELD << line_number << endl;
            exit(EXIT_FAILURE);
        }

        // Converts 'none' to 0 for available seats field
        int number_of_free_seats = (seats_str == "none") ? 0 : stoi(seats_str);

        // Seperates play name from alias, if there is one
        if (play.find('/') != string::npos) {
            vector<string> playParts = split(play, '/');
            playEntries.push_back(PlayEntry(town, theatre, playParts[0], playParts[1], player, number_of_free_seats));
        } else {
            playEntries.push_back(PlayEntry(town, theatre, play, player, number_of_free_seats));
        }
    }
    return playEntries; // Returns class to main function
}

// Fnction which prints all theatres in alphabetical order
void printTheatres(const vector<PlayEntry>& playEntries) {
    vector<string> theatres;

    // Adds each theatre to a vector
    for (const PlayEntry& play : playEntries) {
        theatres.push_back(play.theatre);
    }

    // Sorts theatres alphabetically by name
    sort(theatres.begin(), theatres.end());
    theatres.erase(unique(theatres.begin(), theatres.end()), theatres.end());

    // Prints theatres
    for (const string& theatre : theatres) {
        cout << theatre << endl;
    }
}

// Fnction which prints all plays in alphabetical order
void printPlays(const vector<PlayEntry>& playEntries) {
    vector<string> plays;

    // Adds each play to a vector
    for (const PlayEntry& play : playEntries) {
        string playString = play.play;

        // If play has alias, it is added with a seperator
        if (!play.alias.empty()) {
            playString += " *** " + play.alias;
        }
        plays.push_back(playString);
    }

    // Sorts play alphabetically by name
    sort(plays.begin(), plays.end());

    // Deletes multiple mentions of same play
    plays.erase(unique(plays.begin(), plays.end()), plays.end());

    // Prints plays
    for (const string& printed_play : plays) {
        cout << printed_play << endl;
    }
}

// Fnction which prints all theatres of given play
void printTheatresOfPlay(const vector<PlayEntry>& playEntries, const string& playNameOrAlias) {
    set<string> theatres;

    for (const PlayEntry& play : playEntries) {

        // Checks for allias and splits it from play name
        vector<string> playParts = split(play.play, '/');
        for (const string& part : playParts) {

            // Checks stored data for mentiones of play, or allias and adds those theatres to a string
            if (playNameOrAlias == part || playNameOrAlias == playParts[0] || playNameOrAlias == play.alias) {
                theatres.insert(play.theatre);
            }
        }
    }

    // If theatres have no available seats for specified play,
    // error message is printed, otherwise, all theatres
    // with available seats are printed
    if (theatres.empty()) {
        cout << PLAY_NOT_FOUND << endl;
    } else {
        for (const string& theatre : theatres) {
            cout << theatre << endl;
        }
    }
}

// Fnction which prints all plays in provided theatre
void printPlaysInTheatre(const vector<PlayEntry>& playEntries, const string& theatreName) {
    set<string> uniquePlaysInSelectedTheatre;

    // Add all plays from theatre to a string
    for (const PlayEntry& play : playEntries) {
        if (play.theatre == theatreName) {
            uniquePlaysInSelectedTheatre.insert(play.play);
        }
    }

    // If there are no available seats in theatre,
    // error message is printed, otherwise, all plays
    // with available seats in specified theatre are printed
    if (uniquePlaysInSelectedTheatre.empty()) {
        cout << NOT_AVAILABLE << endl;
    } else {
        for (const string& play : uniquePlaysInSelectedTheatre) {
            cout << play << endl;
        }
    }
}

// Fnction which prints all plays in provided town
void printPlaysInTown(const vector<PlayEntry>& playEntries, const string& townName) {
    // Checks if provided town exists in database
    bool isTownKnown = false;
    for (const PlayEntry& play : playEntries) {
        if (play.town == townName) {
            isTownKnown = true;
            break;
        }
    }

    // If provided town name is not in databse, error message is printed,
    // otherwise, all plays with available seats in specified town are printed
    if (!isTownKnown) {
        cout << TOWN_NOT_FOUND << endl;
    } else {
        map<string, map<string, int>> playsInSelectedTown;

        for (const PlayEntry& play : playEntries) {
            if (play.town == townName) {
                vector<string> playParts = split(play.play, '/');
                for (const string& part : playParts) {
                    playsInSelectedTown[play.theatre][part] = play.availableSeats;
                }
            }
        }

        bool hasPlaysWithSeats = false; // For checking if play has available seats

        for (const auto& entry : playsInSelectedTown) {
            const string& theatre = entry.first;

            for (const auto& playEntry : entry.second) {
                const string& playName = playEntry.first;
                const int totalSeats = playEntry.second;

                // If play has an alias, it is seperated
                string alias = "";
                for (const PlayEntry& play : playEntries) {
                    if (play.town == townName && play.play == playName && !play.alias.empty()) {
                        alias = play.alias;
                        break;
                    }
                }

                // If there are available seats, theatre name
                // and play with alias are printed
                // - there is separator between play and alias
                if (totalSeats > 0) {
                    cout << theatre << " : " << playName;
                    if (!alias.empty()) {
                        cout << " --- " << alias;
                    }
                    cout << " : " << totalSeats << endl;
                    hasPlaysWithSeats = true;
                }
            }
        }

        // If there are no available seats in specified town,
        // error message is printed
        if (!hasPlaysWithSeats) {
            cout << NOT_AVAILABLE << endl;
        }
    }
}

// Fnction which prints all players in provided play
// in provided theatre, if theatre is provided
void printPlayersInPlay(const vector<PlayEntry>& playEntries, const string& input) {
    string playName;
    string theatreName;

    // Extracts play name from input
    istringstream tokenizer(input);
    tokenizer >> playName;

    // If theatre is provided, it is extracted
    string word;
    while (tokenizer >> word) {
        if (!theatreName.empty()) {
            theatreName += " ";
        }
        theatreName += word;
    }

    // Checks that theatre is enclosed in quotation marks
    if (theatreName.size() >= 2 && theatreName.front() == '"' && theatreName.back() == '"') {
        theatreName = theatreName.substr(1, theatreName.size() - 2);
    }

    set<string> theatresAndPlayers;
    bool validTheatreName = false;
    bool validPlayName = false;

    for (const PlayEntry& play : playEntries) {
        if (theatreName.empty() || theatreName == play.theatre) {
            validTheatreName = true;
            if (playName == play.play || playName == play.alias) {
                validPlayName = true;
                theatresAndPlayers.insert(play.theatre + " : " + play.player);
            }
        }
    }

    // Checks if theatre and play are valid input,
    // cecks if there is player for a play in provided theatre,
    // if everything is ok, theatre and player are printed,
    // if not, error message is printed
    if (!validTheatreName) {
        cout << THEATRE_NOT_FOUND << endl;
    } else if (!validPlayName) {
        cout << PLAY_NOT_FOUND << endl;
    } else if (theatresAndPlayers.empty()) {
        cout << PLAYER_NOT_FOUND << endl;
    } else {
        set<string> sortedPlayers(theatresAndPlayers.begin(), theatresAndPlayers.end());

        for (const string& printedPlayer : sortedPlayers) {
            cout << printedPlayer << endl;
        }
    }
}

int main() {
    string filename;
    cout << "Input file: ";
    getline(cin, filename);

    // Calls function to read and check file
    vector<PlayEntry> playEntries = readFile(filename);

    while (true) {
        cout << PROMPT;
        string input;
        getline(cin, input);

        istringstream iss(input);
        string command;
        iss >> command;

        if (command == "quit") {
            break;
        } else if (command == "theatres") {
            // Checks that this command has no other parameters in input
            string next_word;
            if (iss >> next_word) {
                cout << WRONG_PARAMETERS << endl;
                continue;
            }
            printTheatres(playEntries); // Calls function to print all theatres

        } else if (command == "plays") {
            // Checks that this command has no other parameters in input
            string next_word;
            if (iss >> next_word) {
                cout << WRONG_PARAMETERS << endl;
                continue;
            }
            printPlays(playEntries);  // Calls function to print all plays

        } else if (command == "theatres_of_play") {
            // Checks that this command has a parameter in input
            string playNameOrAlias;
            iss >> ws;
            getline(iss, playNameOrAlias);
            if (playNameOrAlias.empty()) {
                cout << WRONG_PARAMETERS << endl;
                continue;
            }

            playNameOrAlias = playNameOrAlias.substr(playNameOrAlias.find_first_not_of(" \t\n"), playNameOrAlias.find_last_not_of(" \t\n") + 1);

            // If play name is enclosed in a  quotation marks, it reads it
            if (playNameOrAlias.size() >= 2 && playNameOrAlias.front() == '"' && playNameOrAlias.back() == '"') {
                playNameOrAlias = playNameOrAlias.substr(1, playNameOrAlias.size() - 2);
            } else if (playNameOrAlias.find(' ') != string::npos) {
                cout << PLAY_NOT_FOUND << endl;
                continue;
            }
            printTheatresOfPlay(playEntries, playNameOrAlias); // Calls function to print theatres of provided play

        } else if (command == "plays_in_theatre") {
            // Checks that this command has a parameter in input
            string theatreName;
            getline(iss, theatreName);
            if (theatreName.empty()) {
                cout << WRONG_PARAMETERS << endl;
                continue;
            }

            theatreName = theatreName.substr(theatreName.find_first_not_of(" \t\n"), theatreName.find_last_not_of(" \t\n") + 1);

            // If theatre name is enclosed in a  quotation marks, it reads it
            if (theatreName.size() >= 2 && theatreName.front() == '"' && theatreName.back() == '"') {
                theatreName = theatreName.substr(1, theatreName.size() - 2);
            } else {
                cout << THEATRE_NOT_FOUND << endl;
                continue;
            }
            printPlaysInTheatre(playEntries, theatreName);

        } else if (command == "plays_in_town") {
            // Checks that this command has a parameters in input
            string townName;
            iss >> ws;
            getline(iss, townName);
            if (townName.empty()) {
                cout << WRONG_PARAMETERS << endl;
                continue;
            }

            townName = townName.substr(townName.find_first_not_of(" \t\n"), townName.find_last_not_of(" \t\n") + 1);

            printPlaysInTown(playEntries, townName);

        } else if (command == "players_in_play") {
            // Checks that this command has a parameters in input
            string playAndTheatreName;
            iss >> ws;
            getline(iss, playAndTheatreName);
            if (playAndTheatreName.empty()) {
                cout << WRONG_PARAMETERS << endl;
                continue;
            }
            printPlayersInPlay(playEntries, playAndTheatreName);

        } else {
            cout << COMMAND_NOT_FOUND << endl;
        }
    }

    return EXIT_SUCCESS;
}
