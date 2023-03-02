class Item:

    def __init__(self, id=None, desc="", quantity=None, price=None):
        self.id = id
        self.desc = desc
        self.quantity = quantity
        self.price = price

    def discount_price(self):
        if self.quantity == 2:
            final_price = (self.price - (self.price * 10) / 100) * self.quantity
            print(final_price)

        elif 3 < self.quantity < 5:
            final_price = (self.price - (self.price * 15) / 100) * self.quantity
            print(final_price)

        elif self.quantity > 5:
            final_price = (self.price - (self.price * 25) / 100) * self.quantity
            print(final_price)
