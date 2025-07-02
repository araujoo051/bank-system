from models import Person, Bank, CurrentAccount, SavingsAccount
from persistence.storage import (
    load_person_from_csv, save_person_to_csv,
    load_banks_from_csv, save_banks_to_csv,
    load_accounts_from_csv, save_accounts_to_csv
)

person_list = load_person_from_csv()
bank_list = load_banks_from_csv()
account_list = load_accounts_from_csv(person_list, bank_list)

def confirm_continue():
    while True:
        choice = input("Do you want to continue? (y/n): ").strip().lower()
        if choice == 'y':
            return True
        elif choice == 'n':
            print("Returning to main menu...")
            return False
        else:
            print("Please enter 'y' or 'n'.")

def menu():
    global person_list, bank_list, account_list  

    while True:
        print("\n=== MAIN MENU ===")
        print("1. Register new person")
        print("2. Register new bank")
        print("3. Create new account (current or savings)")
        print("4. List all people")
        print("5. List all banks")
        print("6. Exit")
        print("7. Load data from CSV")
        print("8. Save data to CSV")

        option = input("Choose an option: ").strip()

        if option == "1":
            person = Person.from_input()
            person_list.append(person)
            print("Person registered successfully.")
            if not confirm_continue():
                continue

        elif option == "2":
            bank = Bank.from_input()
            bank_list.append(bank)
            print("Bank registered successfully.")
            if not confirm_continue():
                continue

        elif option == "3":
            acc_type = input("Account type (c for Current / s for Savings): ").strip().lower()
            if acc_type == "c":
                account = CurrentAccount.from_input(person_list, bank_list)
            elif acc_type == "s":
                account = SavingsAccount.from_input(person_list, bank_list)
            else:
                print("Invalid account type.")
                continue

            if account and account not in account_list:
                account_list.append(account)
                account.holder.add_account(account)
                account.bank.add_account(account)
                print("Account created successfully.")
                if not confirm_continue():
                    continue

        elif option == "4":
            if not person_list:
                print("No people registered.")
            else:
                for person in person_list:
                    print(person.info_person())
                    print(person.info_accounts())
            if not confirm_continue():
                continue

        elif option == "5":
            if not bank_list:
                print("No banks registered.")
            else:
                for bank in bank_list:
                    print(bank.info_bank())
                    print(bank.list_accounts())
            if not confirm_continue():
                continue

        elif option == "6":
            print("Exiting system...")
            save_person_to_csv(person_list)
            save_banks_to_csv(bank_list)
            save_accounts_to_csv(account_list)
            break

        elif option == "7":
            print("Loading data from CSV files...")
            person_list = load_person_from_csv()
            bank_list = load_banks_from_csv()
            account_list = load_accounts_from_csv(person_list, bank_list)
            print("Data loaded successfully.")
            if not confirm_continue():
                continue

        elif option == "8":
            print("Saving data to CSV files...")
            save_person_to_csv(person_list)
            save_banks_to_csv(bank_list)
            save_accounts_to_csv(account_list)
            print("Data saved successfully.")
            if not confirm_continue():
                continue

        else:
            print("Invalid option.")

if __name__ == "__main__":
    menu()
