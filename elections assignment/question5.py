class Store():
    def __init__(self, price, items, date, stock):
        self.price = price
        self.items = items
        self.stock = stock
        self.date = date

        return print(self.price * self.stock)



store1 = Store(20, "cologne", 2025, 5)

print(store1)