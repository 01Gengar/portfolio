#include "queue.hh"
#include <iostream>

// Constructor that initializes the attribute cycle_.
Queue::Queue(unsigned int cycle) : cycle_(cycle) {
    // Initialize the attributes in the constructor
    first_ = nullptr;
    last_ = nullptr;
    is_green_ = false;
}

// Destructor that deletes all the remaining vehicles from the queue.
Queue::~Queue() {
    while (first_ != nullptr) {
        Vehicle *temp = first_;
        first_ = first_->next;
        delete temp;
    }
}

// If the color of traffic light is red, inserts a vehicle to the queue.
void Queue::enqueue(string const& reg) {
    if (!is_green_) {
        Vehicle *newVehicle = new Vehicle;
        newVehicle->reg_num = reg;
        newVehicle->next = nullptr;

        if (!first_) {
            first_ = last_ = newVehicle;
        } else {
            last_->next = newVehicle;
            last_ = newVehicle;
        }
    } else {
        std::cout << "GREEN: The vehicle " << reg << " need not stop to wait" << std::endl;
    }
}

// Switches the color of traffic light from green to red or vice versa.
// If the new color is green, lets at least <cycle_> vehicles
// go on, and finally resets the color to red again.
void Queue::switch_light() {
    is_green_ = !is_green_;

    if (is_green_) {
        std::cout << "GREEN: ";
        if (first_ == nullptr) {
            std::cout << "No vehicles waiting in traffic lights" << std::endl;
        } else {
            std::cout << "Vehicle(s) ";
            for (unsigned int i = 0; i < cycle_; i++) {
                if (first_ == nullptr) {
                    break;
                }

                if (i > 0) {
                    std::cout << " ";
                }
                std::cout << first_->reg_num;

                Vehicle *temp = first_;
                first_ = first_->next;
                delete temp;
            }

            std::cout << " can go on" << std::endl;
            is_green_ = false;
        }
    } else {
        std::cout << "RED: ";
        if (first_ == nullptr) {
            std::cout << "No vehicles waiting in traffic lights" << std::endl;
        } else {
            std::cout << "Vehicle(s) ";
            Vehicle *current = first_;
            while (current != nullptr) {
                std::cout << current->reg_num;
                current = current->next;
                if (current != nullptr) {
                    std::cout << " ";
                }
            }
            std::cout << " waiting in traffic lights" << std::endl;
        }
    }
}

// Resets the attribute cycle_.
void Queue::reset_cycle(unsigned int cycle) {
    cycle_ = cycle;
}

// Prints the color of traffic light and the register numbers of those
// cars that are waiting in the traffic light queue (if any).
void Queue::print() const {
    if (is_green_) {
        std::cout << "GREEN: No vehicles waiting in traffic lights" << std::endl;
    } else {
        std::cout << "RED: ";
        if (first_ == nullptr) {
            std::cout << "No vehicles waiting in traffic lights" << std::endl;
        } else {
            std::cout << "Vehicle(s) ";
            Vehicle *current = first_;
            while (current != nullptr) {
                std::cout << current->reg_num << " ";
                current = current->next;
            }
            std::cout << "waiting in traffic lights" << std::endl;
        }
    }
}
