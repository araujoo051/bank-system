import csv
from models.person import Person
from models.bank import Bank
from models.current_account import CurrentAccount
from models.savings_account import SavingsAccount

def load_person_from_csv(filepath="data/person.csv"):
    person_list = []
    try:
        with open(filepath, newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                person_list.append(Person.from_csv_row(row))
    except FileNotFoundError:
        pass
    return person_list

def save_person_to_csv(person_list, filepath="data/person.csv"):
    with open(filepath, mode='w', newline='') as f:
        writer = csv.writer(f)
        for person in person_list:
            writer.writerow(person.to_csv_row())


def save_banks_to_csv(bank_list, filepath="data/banks.csv"):
    with open(filepath, mode='w', newline='') as f:
        writer = csv.writer(f)
        for bank in bank_list:
            writer.writerow(bank.to_csv_row())

def load_banks_from_csv(filepath="data/banks.csv"):
    bank_list = []
    try:
        with open(filepath, newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                bank_list.append(Bank.from_csv_row(row))
    except FileNotFoundError:
        pass
    return bank_list

def save_accounts_to_csv(account_list, filepath="data/accounts.csv"):
    with open(filepath, mode='w', newline='') as f:
        writer = csv.writer(f)
        for account in account_list:
            writer.writerow(account.to_csv_row())

def load_accounts_from_csv(person_list, bank_list, filepath="data/accounts.csv"):
    account_list = []
    try:
        with open(filepath, newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                account_type = row[0]
                if account_type =="CurrentAccount":
                    account = CurrentAccount.from_csv_row(row, person_list, bank_list)
                elif account_type == "SavingsAccount":
                    account = SavingsAccount.from_csv_row(row, person_list, bank_list)
                else:
                    continue

                if account:
                    account_list.append(account)
                    account.holder.add_account(account)
                    account.bank.add_account(account)
    except FileNotFoundError:
        pass
    return account_list
                    

