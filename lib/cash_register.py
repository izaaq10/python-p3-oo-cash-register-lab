class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.discount = discount
        self.items = []

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        self.items.extend([(title, price)] * quantity)  # Include both title and price in each item

    def apply_discount(self):
        if self.discount > 0:
            self.total -= self.total * (self.discount / 100)
            print(f"After the discount, the total comes to ${self.total:.2f}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if self.items:
            last_item_title, last_item_price = self.items.pop()  # Pop the last item from the list
            self.total -= last_item_price

# Example usage:
cash_register = CashRegister()
cash_register_with_discount = CashRegister(20)

cash_register.add_item("eggs", 1.98)
cash_register.add_item("book", 5.00, 3)
cash_register.add_item("Lucky Charms", 4.50)
cash_register.add_item("Ritz Crackers", 5.00)
cash_register.add_item("Justin's Peanut Butter Cups", 2.50, 2)

cash_register_with_discount.add_item("macbook air", 1000)

cash_register.apply_discount()
cash_register_with_discount.apply_discount()

cash_register.void_last_transaction()
cash_register_with_discount.void_last_transaction()

print("Items in the cash register:")
print(cash_register.items)
print("Total in the cash register:", cash_register.total)

print("Items in the cash register with discount:")
print(cash_register_with_discount.items)
print("Total in the cash register with discount:", cash_register_with_discount.total)
