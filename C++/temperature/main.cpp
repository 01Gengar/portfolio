#include <iostream>

using namespace std;

int main()
{
    cout << "Enter a temperature: ";

    float temp;
    cin >> temp;
    float fah = (temp * 1.8) + 32;
    float cel = (temp - 32) / 1.8;
    cout << temp << " degrees Celsius is " << fah << " degrees Fahrenheit" << endl;
    cout << temp << " degrees Fahrenheit is " << cel << " degrees Celsius" << endl;

    return 0;
}
