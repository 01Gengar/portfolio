#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <map>
#include <vector>
#include <set>

int main() {
    std::string filename;
    std::cout << "Input file: ";
    std::cin >> filename;

    std::ifstream file(filename);
    if (!file.is_open()) {
        std::cerr << "Error! The file " << filename << " cannot be opened." << std::endl;
        return EXIT_FAILURE;
    }

    std::map<std::string, std::vector<int>> wordCounts;

    std::string line;
    int lineNumber = 0;

    while (std::getline(file, line)) {
        lineNumber++;
        std::istringstream iss(line);
        std::string word;
        std::set<std::string> uniqueWords;
        while (iss >> word) {
            uniqueWords.insert(word);
        }
        for (const std::string& uniqueWord : uniqueWords) {
            wordCounts[uniqueWord].push_back(lineNumber);
        }
    }

    file.close();

    for (const auto& entry : wordCounts) {
        const std::string& word = entry.first;
        const std::vector<int>& lines = entry.second;

        std::cout << word << " " << lines.size() << ":";

        for (size_t i = 0; i < lines.size(); ++i) {
            std::cout << " " << lines[i];
            if (i < lines.size() - 1) {
                std::cout << ",";
            }
        }

        std::cout << std::endl;
    }

    return EXIT_SUCCESS;
}
