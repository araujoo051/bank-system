from models.person import Person
from models.bank import Bank
from models.current_account import CurrentAccount
from models.savings_account import SavingsAccount
from persistence.storage import (
    load_people_from_csv, save_people_to_csv,
    load_banks_from_csv, save_banks_to_csv,
    load_accounts_from_csv, save_accounts_to_csv
)

person_list = load_people_from_csv()
bank_list = load_banks_from_csv()
account_list = load_accounts_from_csv(person_list, bank_list)

def menu():
    while True:
        print("\n=== MAIN MENU ===")
        print("1. Register new person")
        print("2. Register new bank")
        print("3. Create new account (current or savings)")
        print("4. List all people")
        print("5. List all banks")
        print("6. Exit")

        option = input("Choose an option: ").strip()

        if option == "1":
            person = Person.from_input()
            person_list.append(person)
            print("Person registered successfully.")

        elif option == "2":
            bank = Bank.from_input()
            bank_list.append(bank)
            print("Bank registered successfully.")

        elif option == "3":
            acc_type = input("Account type (c for Current / s for Savings): ").strip().lower()
            if acc_type == "c":
                account = CurrentAccount.from_input(person_list, bank_list)
            elif acc_type == "s":
                account = SavingsAccount.from_input(person_list, bank_list)
            else:
                print("Invalid account type.")
                continue

            if account:
                account.holder.add_account(account)
                account.bank.add_account(account)
                print("Account created successfully.")

        elif option == "4":
            if not person_list:
                print("No people registered.")
            else:
                for person in person_list:
                    print(person.info_person())
                    print(person.info_accounts())

        elif option == "5":
            if not bank_list:
                print("No banks registered.")
            else:
                for bank in bank_list:
                    print(bank.info_bank())
                    print(bank.list_accounts())

        elif option == "6":
            print("Exiting system...")
            save_people_to_csv(person_list)
            save_banks_to_csv(bank_list)
            save_accounts_to_csv(account_list)
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    menu()
