#include <iostream>

using namespace std;

double factoring_numbers(int number_to_be_factored) {
    double n = 1.0;
    for (int i = 1; i <= number_to_be_factored; ++i) {
        n *= static_cast<double>(i);
        // n = n * i;
    }
    return n;
}

double guess_probability(int all_balls, int drawn_balls) {
    double n = factoring_numbers(all_balls);
    double p = factoring_numbers(drawn_balls);
    double s = factoring_numbers(all_balls - drawn_balls);
    return n / (s * p);
}

int main()
{
    int all_balls, drawn_balls;
    cout << "Enter the total number of lottery balls: ";
    cin >> all_balls;
    cout << "Enter the number of drawn balls: ";
    cin >> drawn_balls;
    if (all_balls <= 0 or drawn_balls <= 0) {
        cout << "The number of balls must be a positive number." << endl;
    }
    else if (all_balls < drawn_balls) {
        cout << "The maximum number of drawn balls is the total amount of balls." << endl;
    }
    else {
        double probability = guess_probability(all_balls, drawn_balls);
        cout << "The probability of guessing all " << drawn_balls << " balls correctly is 1/" << probability << endl;
    }
    return 0;
}
