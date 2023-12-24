#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <vector>

int main() {
    std::string filename;
    std::cout << "Input file: ";
    std::cin >> filename;

    std::ifstream file(filename);
    if (!file.is_open()) {
        std::cerr << "Error! The file " << filename << " cannot be opened." << std::endl;
        return EXIT_FAILURE;
    }

    std::map<std::string, int> scores;

    std::string line;

    while (std::getline(file, line)) {
        size_t colonPos = line.find(':');
        if (colonPos != std::string::npos) {
            std::string name = line.substr(0, colonPos);
            int score = std::stoi(line.substr(colonPos + 1));
            scores[name] += score;
        }
    }

    file.close();

    std::cout << "Final scores:" << std::endl;
    for (const auto& entry : scores) {
        std::cout << entry.first << ": " << entry.second << std::endl;
    }

    return EXIT_SUCCESS;
}
