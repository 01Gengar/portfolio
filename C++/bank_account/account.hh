#ifndef ACCOUNT_HH
#define ACCOUNT_HH

#include <string>

class Account
{
public:
    // Constructor
    Account(const std::string& owner, bool has_credit = false);

    // More methods
    void print() const;

    // Member function to set credit limit
    void set_credit_limit(int limit);

    // Member function to save money
    void save_money(int amount);

    // Member function to take money
    void take_money(int amount);

    // Member function to transfer money to another account
    void transfer_to(Account& target_account, int amount);

private:
    // Generates IBAN (based on running_number_ below).
    // Allows no more than 99 accounts.
    void generate_iban();

    std::string iban_;

    // Used for generating IBAN.
    // Static keyword means that the value of running_number_ is the same for
    // all Account objects.
    // In other words, running_number_ is a class-wide attribute, there is
    // no own copies of it for each object of the class.
    static int running_number_;

    // More attributes/methods
    std::string owner_name;
    double balance;
    bool is_credit_card;
    int credit_limit;

};

#endif // ACCOUNT_HH
