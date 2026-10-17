#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=None):
        # If no input is provided, default to 0
        if discount is None:
            self.discount = 0
        else:
            self.discount = discount
            
        self.total = 0
        self.items = []
        self.previous_transactions = []

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        # Ensure discount is an integer between 0 and 100 inclusive
        if isinstance(value, int) and 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")
            self._discount = 0 # Fallback so the program doesn't crash

    def add_item(self, item, price, quantity=1):
        """Adds an item, updates total, and saves the transaction."""
        # Update total price
        self.total += (price * quantity)
        
        # Add item to the items array (once per quantity)
        for _ in range(quantity):
            self.items.append(item)
            
        # Save the transaction object
        transaction = {
            "item": item,
            "price": price,
            "quantity": quantity
        }
        self.previous_transactions.append(transaction)

    def apply_discount(self):
        """Applies the percentage discount to the total."""
        # If there are no items OR the discount is 0, print the error
        if len(self.items) == 0 or self.discount == 0:
            print("There is no discount to apply.")
            return

        # Calculate the discount amount
        discount_amount = self.total * (self.discount / 100)
        self.total -= discount_amount

        # Print the exact success message the test expects
        print(f"After the discount, the total comes to ${self.total:.0f}.")
        
    def void_last_transaction(self):
        """Removes the last transaction and reverts the total and items."""
        if len(self.previous_transactions) == 0:
            print("No transactions to void.")
            return

        last_transaction = self.previous_transactions.pop()
        
        # Revert the total price
        self.total -= (last_transaction["price"] * last_transaction["quantity"])
        
        # Remove the items from the list
        for _ in range(last_transaction["quantity"]):
            if last_transaction["item"] in self.items:
                self.items.remove(last_transaction["item"])