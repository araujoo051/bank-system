from models.bank_account import BankAccount

class SavingsAccount(BankAccount):
    def __init__(self, holder, bank, number, balance=0.0, password="", revenue: float = 0.0):
        super().__init__(holder, bank, number, balance, password)
        self._revenue = revenue
        self._monthly_sakes = 0

    def withdraw(self, amount):
        if self._monthly_sakes < 3 and amount <= self._balance:
            self._balance -= amount
            self._monthly_sakes += 1
            return f"Withdrawal successful. New balance: {self._balance}"
        else:
            return "Insufficient balance for withdrawal."

    def new_month(self):
        self._balance += self._balance * self._revenue
        self._monthly_sakes = 0

    @property
    def revenue(self):
        return self._revenue
    
    @revenue.setter
    def revenue(self, value):
        if value < 0:
            raise ValueError("Revenue must be non-negative.")
        self._revenue = value
    
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
        revenue = float(input("Monthly interest rate (e.g. 0.02 for 2%): "))

        return cls(holder, bank, number, balance, password, revenue)


