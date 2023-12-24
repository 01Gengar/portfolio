#include <iostream>
#include <string>
#include <algorithm>
#include <random>

int main()
{
    // This is a random number generator that should be given as parameter to the
    // function of the algorithm library to shuffle letters
    std::minstd_rand generator;

    std::cout << "Enter some text. Quit by entering the word \"END\"." << std::endl;
    std::string word;

    while (std::cin >> word)
    {
        if (word == "END")
        {
            return EXIT_SUCCESS;
        }

        if (word.length() > 3)
        {
            // Extract the first and last characters of the word.
            char first = word.front();
            char last = word.back();

            // Shuffle the middle characters of the word (excluding the first and last characters).
            std::string middle = word.substr(1, word.length() - 2);
            std::shuffle(middle.begin(), middle.end(), generator);

            // Reconstruct the word with shuffled middle characters.
            word = first + middle + last;
        }


        std::cout << word << std::endl;
    }
}
