#include <iostream>
using namespace std;


int main()
{
    cout << "Enter a number: ";
    unsigned int n;
    cin >> n;
    int result = n * n * n;
    if (n > 4641 or result < 0) {
        cout << "Error! The cube of " << n << " is not " << result << "." << endl;
    }
    else {
        cout << "The cube of " << n << " is " << result << "." << endl;
    }

    return 0;
}
