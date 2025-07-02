from models.bank_account import BankAccount
from models.person import Person
from models.bank import Bank

class CurrentAccount(BankAccount):
    def __init__(self, holder, bank, number, balance=0.0, password="", monthly_fee: float = 0.0):
        super().__init__(holder, bank, number, balance, password)
        self._monthly_fee = monthly_fee

    def withdraw(self, amount: float):
        if amount <= self._balance:
            self._balance -= amount
            return f"Withdrawal successful. New balance: {self._balance:.2f}"
        else:
            return "Insufficient balance for withdrawal."
        
    def new_month(self):
        self._balance -= self._monthly_fee
        if self._balance < 0:
            return "Balance is negative after monthly fee deduction."
        return f"Monthly fee deducted. New balance: R$ {self._balance:.2f}"
        
    def info_account(self):
        return (
            f"{self.__class__.__name__} - Number: {self._number}, "
            f"Balance: R${self._balance:.2f}, Bank: {self._bank.name}"
        )
    
    @property
    def monthly_fee(self):
        return self._monthly_fee

    @monthly_fee.setter
    def monthly_fee(self, value):
        if value < 0:
            raise ValueError("Monthly fee must be non-negative.")
        self._monthly_fee = value
    
    def to_csv_row(self):
        return [
            "CurrentAccount",
            self._holder.cpf,
            self._bank.cnpj,
            str(self._number),
            str(self._balance),
            self._password,
            str(self.monthly_fee)
        ]

    @classmethod
    def from_csv_row(cls, row, person_list, bank_list):
        _, cpf, cnpj, number, balance, password, monthly_fee = row

        holder = next((p for p in person_list if p.cpf == cpf), None)
        bank = next((b for b in bank_list if b.cnpj == cnpj), None)

        if not holder or not bank:
            return None

        return cls(holder, bank, int(number), float(balance), password, float(monthly_fee))

    @classmethod
    def from_input(cls, person_list, bank_list):
        print("Creating a new Current Account...")

        cpf = input("CPF from holder: ").strip()
        holder = next((p for p in person_list if p.cpf == cpf), None)
        if not holder:
            print("Person not found.")
            return None

        cnpj = input("CNPJ from bank: ").strip()
        bank = next((b for b in bank_list if b.cnpj == cnpj), None)
        if not bank:
            print("Bank not found.")
            return None

        number = int(input("New Account Number: "))
        balance = float(input("Opening balance $: "))
        password = input("New Password: ")
        monthly_fee = float(input("Monthly Fee: "))

        return cls(holder, bank, number, balance, password, monthly_fee)