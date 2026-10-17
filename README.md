# Object-Oriented Programming (OOP) Part 2 - Cash Register

## Description

This project is a Python-based simulation of an e-commerce cash register. It demonstrates advanced Object-Oriented Programming (OOP) concepts, specifically the use of Python properties (`@property` and `@setter`) for data validation, as well as managing state through lists and dictionaries.

The `CashRegister` class allows users to add items to a cart, apply percentage-based discounts, and void previous transactions while keeping track of the running total.

## Features

**Initialization**: Accepts an optional `discount` argument (defaults to 0). Initializes `total` (0), `items` (empty list), and `previous_transactions` (empty list).

**Discount Validation**: Uses properties to ensure the discount is an integer between 0 and 100. Prints `"Not valid discount"` if the input is invalid.

**Add Items**: `add_item(item, price, quantity)` updates the total, appends items to the cart, and records the transaction.

**Apply Discount**: `apply_discount()` calculates the percentage off the total, removes the last transaction, and prints a success message (or an error if the cart is empty/no discount).

**Void Transaction**: `void_last_transaction()` removes the most recent transaction, reverting both the total price and the items list.

## Requirements

Python 3.8 or higher
`pytest` for running the test suite

## Installation & Setup

To get this project running on your local machine, follow these steps:

1. **Clone the repository:**

```bash
   git clone https://github.com/YourUsername/oop-p2-cash-register-lab.git
   cd oop-p2-cash-register-lab
```

## Set up the environment: (Pipenv)

```bash
pipenv install
pipenv shell
```

## Usage & Testing

This lab is test-driven. To verify that the CashRegister class is working correctly, run the test suite from the root directory:

```bash
pytest -x lib/testing/
```

## Contributing

This project was completed as part of a Moringa School Object-Oriented Programming lab.

## Screenshot

![Screenshot](img/Screenshot%20From%202026-10-17%2016-18-51.png)

## License

This project is open-source and available under the MIT License.