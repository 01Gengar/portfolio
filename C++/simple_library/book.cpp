#include "book.hh"
#include <iostream>

Book::Book(const std::string& author, const std::string& title)
    : author_(author), title_(title), is_available_(true)
{
}

bool Book::loan(const Date& date)
{
    if (is_available_)
    {
        loaned_date_ = date;
        // Advance the return date by 28 days.
        return_date_ = date;
        return_date_.advance(28);
        is_available_ = false;
        return true;
    }
    else
    {
        std::cout << "Already loaned: cannot be loaned" << std::endl;
        return false;
    }
}

bool Book::renew()
{
    if (!is_available_)
    {
        // Advance the return date by another 28 days.
        return_date_.advance(28);
        return true;
    }
    else
    {
        std::cout << "Not loaned: cannot be renewed" << std::endl;
        return false;
    }
}

bool Book::give_back()
{
    is_available_ = true;
    return true;
}

void Book::print() const
{
    std::cout << author_ << " : " << title_ << std::endl;
    if (is_available_)
    {
        std::cout << "- available" << std::endl;
    }
    else
    {
        std::cout << "- loaned: ";
        loaned_date_.print();
        std::cout << "- to be returned: ";
        return_date_.print();
    }
}
