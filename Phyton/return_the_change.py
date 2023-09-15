def main():
    # Reading the user input
    receipt = input("Purchase price: ")
    money = input("Paid amount of money: ")

    # Let's save these values
    price = int(receipt)
    payment = int(money)

    # Let's first set condition when there is no need for any change
    if payment <= price:
        print("No change")
        return

    # Let's get on with calculations
    else:
        ten_bill = int((payment - price) / 10)
        five_bill = int((payment - (ten_bill * 10) - price) / 5)
        two_bill = int((payment - (ten_bill * 10) - (five_bill * 5) - price) / 2)
        one_bill = int(payment - (ten_bill * 10) - (five_bill * 5) - (two_bill * 2) - price)
        print("Offer change:")
        if ten_bill > 0:
            print(ten_bill, "ten-euro notes")
        if five_bill > 0:
            print(five_bill, "five-euro notes")
        if two_bill > 0:
            print(two_bill, "two-euro coins")
        if one_bill > 0:
            print(one_bill, "one-euro coins")


if __name__ == "__main__":
    main()
