#include <cmath>
#include <iostream>

using namespace std;

int main()
{
    cout << "Enter a positive number: ";

    int n;
    cin >> n;
    if (n <= 0) {
        cout << "Only positive numbers accepted" << endl;
    }
    else {
        for (int i = sqrt(n); i > 0; --i) {
            if (n % i == 0) {
                int a = i;
                int b = n / a;
                cout << n << " = " << a << " * " << b << endl;
                break;
            }
        }
    }

    return 0;
}
