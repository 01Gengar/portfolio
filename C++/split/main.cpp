#include <iostream>
#include <string>
#include <vector>

std::vector<std::string> split(const std::string& input, char delimiter, bool skip_empty = false) {
    std::vector<std::string> parts;
    std::string part;
    bool prev_delimiter = true;

    for (char c : input) {
        if (c == delimiter) {
            if (!skip_empty || !prev_delimiter) {
                parts.push_back(part);
            }
            part.clear();
            prev_delimiter = true;
        } else {
            part += c;
            prev_delimiter = false;
        }
    }

    if (!skip_empty || !prev_delimiter) {
        parts.push_back(part);
    }

    return parts;
}

int main()
{
    std::string line = "";
    std::cout << "Enter a string: ";
    getline(std::cin, line);
    std::cout << "Enter the separator character: ";
    char separator = getchar();

    std::vector< std::string > parts  = split(line, separator);
    std::cout << "Splitted string including empty parts: " << std::endl;
    for( auto part : parts ) {
        std::cout << part << std::endl;
    }

    std::vector< std::string > parts_no_empty  = split(line, separator, true);
    std::cout << "Splitted string ignoring empty parts: " << std::endl;
    for( auto part : parts_no_empty ) {
        std::cout << part << std::endl;
    }
}
