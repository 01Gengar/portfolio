#ifndef BOOK_HH
#define BOOK_HH

#include "date.hh"
#include <string>

class Book
{
public:
    // Constructor for the Book class.
    Book(const std::string& author, const std::string& title);

    // Loan the book on the given date.
    bool loan(const Date& date);

    // Renew the loaned book.
    bool renew();

    // Give back the book.
    bool give_back();

    // Print the book's information.
    void print() const;

private:
    std::string author_;
    std::string title_;
    Date loaned_date_;
    Date return_date_;
    bool is_available_;
};

#endif // BOOK_HH
