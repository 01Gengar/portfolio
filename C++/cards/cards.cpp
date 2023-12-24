#include "cards.hh"
#include <iostream>

// Constructor: Initializes the top item as nullptr.
Cards::Cards() : top_(nullptr) {}

// Get the topmost card for testing.
Card_data *Cards::get_topmost() {
    return top_;
}

// Add a new card with the given id as the topmost element.
void Cards::add(int id) {
    Card_data* newCard = new Card_data;
    newCard->data = id;
    newCard->next = top_;
    top_ = newCard;
}

// Prints the content of the data structure from top to bottom.
void Cards::print_from_top_to_bottom(std::ostream& s) {
    Card_data* current = top_;
    int ordinal = 1;
    while (current) {
        s << ordinal << ": " << current->data << std::endl;
        current = current->next;
        ordinal++;
    }
}

// Removes the topmost card and passes its id in the reference parameter.
// Returns false if the data structure is empty, otherwise returns true.
bool Cards::remove(int& id) {
    if (top_) {
        Card_data* temp = top_;
        id = temp->data;
        top_ = top_->next;
        delete temp;
        return true;
    }
    return false;
}

// Moves the last element of the data structure as the first one.
// Returns false if the data structure is empty, otherwise returns true.
bool Cards::bottom_to_top() {
    if (!top_ || !top_->next) {
        // If the deck is empty or contains only one card, no need to move.
        return false;
    }

    Card_data* current = top_;
    while (current->next->next) {
        current = current->next;
    }

    // Move the last card to the top.
    Card_data* lastCard = current->next;
    current->next = nullptr;

    // Update the top pointer.
    lastCard->next = top_;
    top_ = lastCard;
    return true;
}

// Moves the first element of the data structure as the last one.
// Returns false if the data structure is empty, otherwise returns true.
bool Cards::top_to_bottom() {
    if (!top_ || !top_->next) {
        // If the deck is empty or contains only one card, no need to move.
        return false;
    }

    Card_data* current = top_;
    Card_data* newTop = top_->next;

    while (current->next) {
        current = current->next;
    }

    // Move the first card to the bottom.
    Card_data* firstCard = top_;
    firstCard->next = nullptr;
    current->next = firstCard;
    top_ = newTop;

    return true;
}

// Prints the content of the data structure from bottom to top using recursion.
void Cards::print_from_bottom_to_top(std::ostream& s) {
    recursive_print(top_, s);
}

// Recursive function to print the content from bottom to top.
int Cards::recursive_print(Card_data* top, std::ostream& s) {
    if (!top) {
        return 1;
    }
    int ordinal = recursive_print(top->next, s);
    s << ordinal << ": " << top->data << std::endl;
    return ordinal + 1;
}

// Destructor: Deallocates memory for all cards.
Cards::~Cards() {
    while (top_) {
        Card_data* temp = top_;
        top_ = top_->next;
        delete temp;
    }
}
