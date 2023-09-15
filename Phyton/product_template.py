# Template for the product assignment.


class Product:
    """
    This class defines a simplified product for sale in a store.
    """
    def __init__(self, product_name, price, sale_percentage=0.0):
        """
        A product object is initialized with the name, price and
        the sale% which is 0.0 in the creation.

        :param product_name: str, Name of the product.
        :param price: float, Price of the product
        :param sale_percentage: float, Discount percentage
                                        for product on sale.
        """
        self.__product = product_name
        self.__price = price
        self.__percentage = sale_percentage

    def printout(self):
        """
        When a product's data is needed to be printed on
        screen this method will handle it.
        """
        print(self.__product)
        print(f"  price: {self.__price:.2f}")
        print(f"  sale%: {self.__percentage:.2f}")

    def get_price(self):
        """
        Calculates new price after discount.

        :return: float, New, discounted price.
        """
        new_price = self.__price - (self.__price * self.__percentage / 100)
        return new_price

    def set_sale_percentage(self, sale_percentage):
        """
        Sets discount percentage.

        :param sale_percentage: float, Discount percentage.
        """
        self.__percentage = sale_percentage


def main():

    test_products = {
        "milk":   1.00,
        "sushi": 12.95,
    }

    for product_name in test_products:
        print("=" * 20)
        print(f"TESTING: {product_name}")
        print("=" * 20)

        prod = Product(product_name, test_products[product_name])

        prod.printout()
        print(f"Normal price: {prod.get_price():.2f}")

        print("-" * 20)

        prod.set_sale_percentage(10.0)
        prod.printout()
        print(f"Sale price: {prod.get_price():.2f}")

        print("-" * 20)

        prod.set_sale_percentage(25.0)
        prod.printout()
        print(f"Sale price: {prod.get_price():.2f}")

        print("-" * 20)


if __name__ == "__main__":
    main()
