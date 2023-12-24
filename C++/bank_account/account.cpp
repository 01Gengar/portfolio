#include "account.hh"
#include <iostream>

Account::Account(const std::string& owner, bool has_credit) :
    owner_name(owner),
    balance(0),
    is_credit_card(has_credit)
{
    generate_iban();
}

// Setting initial value for the static attribute running_number_
int Account::running_number_ = 0;

void Account::generate_iban()
{
    ++running_number_;
    std::string suffix = "";
    if(running_number_ < 10)
    {
        suffix.append("0");
    }
    else if(running_number_ > 99)
    {
        std::cout << "Too many accounts" << std::endl;
    }
    suffix.append(std::to_string(running_number_));

    iban_ = "FI00 1234 ";
    iban_.append(suffix);
}

void Account::print() const {
    std::cout << owner_name << " : " << iban_ << " : " << balance << " euros" << std::endl;
}

void Account::set_credit_limit(int limit) {
    if (is_credit_card) {
        credit_limit = limit;
    } else {
        std::cout << "Cannot set credit limit: the account has no credit card" << std::endl;
    }
}

void Account::save_money(int amount) {
    balance += amount;
}

void Account::take_money(int amount) {
    if (is_credit_card) {
        if (balance + credit_limit >= amount) {
            balance -= amount;
            std::cout << amount << " euros taken: new balance of " << iban_ << " is " << balance << " euros" << std::endl;
        } else {
            std::cout << "Cannot take money: credit limit overflow" << std::endl;
        }
    } else {
        if (balance >= amount) {
            balance -= amount;
            std::cout << amount << " euros taken: new balance of " << iban_ << " is " << balance << " euros" << std::endl;
        } else {
            std::cout << "Cannot take money: balance underflow" << std::endl;
        }
    }
}

void Account::transfer_to(Account& target_account, int amount) {
    if (balance >= amount || (is_credit_card && balance + credit_limit >= amount)) {
        if (is_credit_card) {
            balance -= amount;
            target_account.balance += amount;
            std::cout << amount << " euros taken: new balance of " << iban_ << " is " << balance << " euros" << std::endl;
        } else {
            if (balance >= amount) {
                balance -= amount;
                target_account.balance += amount;
                std::cout << amount << " euros taken: new balance of " << iban_ << " is " << balance << " euros" << std::endl;
            } else {
                std::cout << "Cannot take money: balance underflow" << std::endl;
                std::cout << "Transfer from " << iban_ << " failed" << std::endl;
            }
        }
    } else {
        std::cout << "Cannot take money: credit limit overflow" << std::endl;
        std::cout << "Transfer from " << iban_ << " failed" << std::endl;
    }
}
