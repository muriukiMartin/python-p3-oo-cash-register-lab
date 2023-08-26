#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount = 0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

    def add_item(self, item, price, quantity = 1):
        self.total += price * quantity
        self.items.extend([item] * quantity)
        self.previous_transactions.append({"item": item, "quantity": quantity, "price": price})

    def apply_discount(self):
        if self.discount:
          self.total -= int(self.total * (self.discount/100))
          print(f"After the discount, the total comes to ${self.total}.")
        else:
         print(f"There is no discount to apply.")
         return self.total
        
    def void_last_transaction(self):
       self.total -= (self.previous_transactions[-1]["price"] * self.previous_transactions[-1]["quantity"])
         