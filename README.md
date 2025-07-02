# Banking System in Python

This is a simple banking system implemented in Python. It allows registering people, banks, and bank accounts (current and savings accounts), with data persistence through CSV files.

## Features

- Register People (name, surname, age, CPF)
- Register Banks (name, CNPJ, bank number)
- Create Bank Accounts:
  - Current Account with monthly fee
  - Savings Account with monthly revenue and withdrawal limit
- List registered People, Banks, and Accounts
- Data persistence in CSV files (load and save)
- Simple input validation
- Interactive terminal menu

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/your_username/bank-system.git
cd bank-system
```
Make sure Python 3 is installed.

Run the program:

python main.py

Use the interactive menu to:

- Register people and banks

- Create current or savings accounts

- List registered entities

- Load or save data to CSV files

## CSV Data Files:
- person.csv: stores registered people data

- banks.csv: stores registered bank data

- accounts.csv: stores created accounts data

## Persistence Details:
- On startup, the program attempts to load data from CSV files if they exist.

- Data changes can be saved anytime through the menu.

- CSV format allows easy manual inspection and modification.

## Dependencies
- Only standard Python libraries are used (no external packages).

# Contribution
Feel free to fork the repo and submit pull requests. Bug reports and feature suggestions are welcome via issues.

---
