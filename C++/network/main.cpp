#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>

const std::string HELP_TEXT = "S = store id1 id2\nP = print id\n"
                              "C = count id\nD = depth id\n";

struct Marketer {
    std::string id;
    std::vector<Marketer> recruits;
    int depth;
};

std::map<std::string, Marketer> network;

// Function to print the subnetwork of a person
void printSubnetwork(const std::string& id, int depth) {
    if (network.find(id) == network.end()) {
        return; // ID not found, return
    }

    // Print the current marketer with the specified depth
    for (int i = 0; i < depth; ++i) {
        std::cout << "..";
    }
    std::cout << network[id].id << std::endl;

    // Recursively print recruits of this marketer with increased depth
    for (const Marketer& recruit : network[id].recruits) {
        printSubnetwork(recruit.id, depth + 1);
    }
}

// Function to count the size of a subnetwork
int countSubnetworkSize(const std::string& id) {
    if (network.find(id) == network.end()) {
        return 0; // ID not found, return 0
    }

    // Count the person
    int size = 1;

    // Recursively count recruits in lower levels
    for (const Marketer& recruit : network[id].recruits) {
        size += countSubnetworkSize(recruit.id);
    }

    return size;
}

// Function to calculate the depth of a subnetwork
int calculateSubnetworkDepth(const std::string& id) {
    if (network.find(id) == network.end()) {
        return 0; // ID not found, return 0
    }

    int maxDepth = 0;

    // Recursively calculate the depth for each recruit
    for (const Marketer& recruit : network[id].recruits) {
        maxDepth = std::max(maxDepth, calculateSubnetworkDepth(recruit.id));
    }

    return maxDepth + 1; // Increase the maximum depth by 1 for the current person
}

int main() {
    while (true) {
        std::string line;
        std::cout << "> ";
        getline(std::cin, line);
        std::vector<std::string> parts;
        size_t pos = 0;

        // Split the input line into parts
        while ((pos = line.find(" ")) != std::string::npos) {
            parts.push_back(line.substr(0, pos));
            line.erase(0, pos + 1);
        }
        parts.push_back(line);

        // Allowing empty inputs
        if (parts.size() == 0) {
            continue;
        }

        std::string command = parts.at(0);

        if (command == "S" || command == "s") {
            if (parts.size() != 3) {
                std::cout << "Erroneous parameters!" << std::endl << HELP_TEXT;
                continue;
            }
            std::string id1 = parts.at(1);
            std::string id2 = parts.at(2);

            if (network.find(id1) == network.end()) {
                Marketer newRecruiter;
                newRecruiter.id = id1;
                network[id1] = newRecruiter;
            }

            if (network.find(id2) == network.end()) {
                Marketer newRecruit;
                newRecruit.id = id2;
                network[id2] = newRecruit;
            }

            // Add the recruit to the recruiter's list
            network[id1].recruits.push_back(network[id2]);
        } else if (command == "P" || command == "p") {
            if (parts.size() != 2) {
                std::cout << "Erroneous parameters!" << std::endl << HELP_TEXT;
                continue;
            }
            std::string id = parts.at(1);

            if (network.find(id) != network.end()) {
                // Print the network starting from the specified ID
                printSubnetwork(id, 0);
            } else {
                std::cout << "Person not found in the network." << std::endl;
            }
        } else if (command == "C" || command == "c") {
                if (parts.size() != 2) {
                    std::cout << "Erroneous parameters!" << std::endl << HELP_TEXT;
                    continue;
                }
                std::string id = parts.at(1);

                if (network.find(id) == network.end()) {
                    std::cout << "Person not found!" << std::endl;
                } else {
                    // Count the size of the subnetwork of the specified person
                    int subnetworkSize = countSubnetworkSize(id) - 1;
                    std::cout << subnetworkSize << std::endl;
                }
            } else if (command == "D" || command == "d") {
            if (parts.size() != 2) {
                std::cout << "Erroneous parameters!" << std::endl << HELP_TEXT;
                continue;
            }
            std::string id = parts.at(1);

            if (network.find(id) == network.end()) {
                std::cout << "Person not found!" << std::endl;
            } else {
                // Calculate the depth of the subnetwork of the specified person
                int subnetworkDepth = calculateSubnetworkDepth(id);
                std::cout << subnetworkDepth << std::endl;
            }
        } else if (command == "Q" || command == "q") {
            return EXIT_SUCCESS;
        } else {
            std::cout << "Erroneous command!" << std::endl << HELP_TEXT;
        }
    }
}
