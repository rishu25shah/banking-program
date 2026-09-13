# Python Banking Program

A simple console-based banking application built with Python.
This project allows users to check their balance, deposit money, withdraw money, and exit the program through an interactive menu.

## Project Overview

The Banking Program is a beginner-friendly Python project designed to demonstrate fundamental programming concepts such as:

* Functions
* Variables
* Conditional statements
* `while` loops
* `match-case`
* User input
* Arithmetic operations
* Function parameters and return values
* Basic input validation

The program starts with a balance of `$0.00` and allows the user to perform basic banking operations.

## Features

### 1. Show Balance

Displays the user's current account balance with two decimal places.

### 2. Deposit Money

Allows the user to enter an amount to deposit.

* Amount must be greater than `0`.
* Invalid amounts are rejected.

### 3. Withdraw Money

Allows the user to withdraw money from their account.

* The withdrawal amount must be greater than `0`.
* The user cannot withdraw more money than their available balance.
* Insufficient funds are handled with an error message.

### 4. Exit

Closes the banking program and displays a thank-you message.

## Technologies Used

* Python 3
* Standard Python libraries only
* No external dependencies

## Project Structure

```text
Banking-Program/
│
├── banking_program.py
└── README.md
```

## Requirements

Make sure Python 3 is installed on your computer.

You can check your Python version using:

```bash
python --version
```

or:

```bash
python3 --version
```

## How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/banking-program.git
```

### 2. Open the Project Folder

```bash
cd banking-program
```

### 3. Run the Program

```bash
python banking_program.py
```

## How the Program Works

When the program starts, it displays the following menu:

```text
***************************
     BANKING PROGRAM
***************************
1.SHOW BALANCE
2.DEPOSIT
3.WITHDRAW
4.EXIT

Enter your choice (1-4):
```

### Example: Checking Balance

```text
YOUR BALANCE IS:$0.00
```

### Example: Depositing Money

```text
ENTER THE AMOUNT TO DEPOSIT:500
```

The balance becomes:

```text
YOUR BALANCE IS:$500.00
```

### Example: Withdrawing Money

```text
ENTER THE AMOUNT TO WITHDRAW:200
```

The remaining balance becomes:

```text
YOUR BALANCE IS:$300.00
```

### Example: Insufficient Funds

If the user tries to withdraw more than the available balance:

```text
INSUFFICIENT FUNDS!
```

## Functions

The program is divided into separate functions to make the code easier to understand and maintain.

### `show_balance(balance)`

Displays the current account balance.

```python
def show_balance(balance):
    print(f"YOUR BALANCE IS:${balance:.2f}")
```

### `deposit()`

Takes the deposit amount from the user and returns it if it is valid.

```python
def deposit():
    amount = float(input("ENTER THE AMOUNT TO DEPOSIT:"))
```

### `withdraw(balance)`

Takes the withdrawal amount and checks whether the user has sufficient funds.

```python
def withdraw(balance):
```

### `main()`

Controls the main banking program and menu.

```python
def main():
```

## Concepts Learned

| Concept        | Usage                                |
| -------------- | ------------------------------------ |
| Functions      | Separate banking operations          |
| Parameters     | Passing balance to functions         |
| Return values  | Returning deposit/withdrawal amounts |
| `if-elif-else` | Input validation                     |
| `while` loop   | Keeping the program running          |
| `match-case`   | Handling menu choices                |
| `float`        | Handling monetary values             |
| f-strings      | Formatting balance                   |
| `__name__`     | Starting the program                 |

## Future Improvements

This project can be extended with more advanced banking features, such as:

* PIN/password authentication
* Multiple user accounts
* Saving account data to a file
* SQLite database integration
* Transaction history
* Transfer money between accounts
* Monthly transaction reports
* Graphical User Interface (GUI)
* Web-based banking application
* Unit testing

## Current Limitations

This is an educational project and is **not intended for real banking use**.

Currently:

* The balance is stored only while the program is running.
* Data is lost when the program is closed.
* There is no user authentication.
* There is no database.
* The program uses basic input validation.

## Project Goal

The main goal of this project is to practice Python fundamentals and programming logic by creating a simple real-world application.

## Author

**Rishu Shah**

A beginner Python project created for learning and practicing programming concepts.

## License

This project is created for educational purposes. You are free to use, modify, and improve the code for learning.
