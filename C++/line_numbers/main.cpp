#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    string input_file_name = "" ;
    string output_file_name = "" ;
    cout << "Input file: " ;
    getline ( cin >> ws , input_file_name );
    cout << "Output file: " ;
    cin >> output_file_name;
    ifstream file_object ( input_file_name );
    if ( file_object ) {
        string line ;
        int counter = 1;
        ofstream outputFile(output_file_name);
        while ( getline ( file_object , line ) ) {
            outputFile << counter << " " << line << endl;
            counter++;
        }
        file_object . close ();
        outputFile.close();
    } else {
        cout << "Error! The file " << input_file_name << " cannot be opened." << endl;
        return EXIT_FAILURE;
    }
}
