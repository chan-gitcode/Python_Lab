class Product:
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total_price(self):
        total = self.price * self.quantity
        return total

    def display_info(self):
        print(
            f"Product: {self.name}\nPrice: {self.price}\nQuantity: {self.quantity}\nTotal Price= {self.get_total_price()}"
        )


book = Product(name="Book 1", price=99.9, quantity=10)
book.display_info()
