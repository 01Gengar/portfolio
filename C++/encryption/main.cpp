#include <iostream>
#include <string>
#include <cctype>
#include <cstdlib>

using namespace std;

int main()
{
    string encryption_key, original_text, encrypted_text;
    cout << "Enter the encryption key: ";
    cin >> encryption_key;
    if (encryption_key.length() != 26) {
        cout << "Error! The encryption key must contain 26 characters." << endl;
        exit(EXIT_FAILURE);
    }
    else {
        for (char c : encryption_key) {
            if (!islower(c)) {
                cout << "Error! The encryption key must contain only lower case characters." << endl;
                exit(EXIT_FAILURE);
            }
        }
        bool letterPresent[26] = {false};
        for (char c : encryption_key) {
            letterPresent[c - 'a'] = true;
        }
        for (bool present : letterPresent) {
            if (!present) {
                cout << "Error! The encryption key must contain all alphabets a-z." << endl;
                exit(EXIT_FAILURE);
            }
        }
        cout << "Enter the text to be encrypted: ";
        cin >> original_text;
        for (char c : original_text) {
            if (!islower(c)) {
                cout << "Error! The text to be encrypted must contain only lower case characters." << endl;
                exit(EXIT_FAILURE);
            }
        }
        for (char &c : original_text) {
            if (islower(c)) {
                int index = c - 'a';
                c = encryption_key[index];
            }
        }
        cout << "Encrypted text: " << original_text << endl;
    }
    return 0;
}
