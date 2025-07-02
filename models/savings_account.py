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

    def info_account(self):
        return (
            f"{self.__class__.__name__} - Number: {self._number}, "
            f"Balance: R${self._balance:.2f}, Bank: {self._bank.name}, "
            f"Monthly Revenue: {self._revenue:.4f}, "
            f"Monthly Withdrawals: {self._monthly_sakes}"
        )

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
        print("Creating a new Savings Account...")

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
    
    def to_csv_row(self):
        return [
            "SavingsAccount",
            self._holder.cpf,
            self._bank.cnpj,
            str(self._number),
            str(self._balance),
            self._password,
            str(self._revenue),
            str(self._monthly_sakes)
        ]
    
    @classmethod
    def from_csv_row(cls, row, person_list, bank_list):
        _, cpf, cnpj, number, balance, password, revenue, monthly_sakes = row
        holder = next((p for p in person_list if p.cpf == cpf), None)
        bank = next((b for b in bank_list if b.cnpj == cnpj), None)

        if not holder or not bank:
            return None
        
        account = cls(holder, bank, int(number), float(balance), password, float(revenue))
        account._monthly_sakes = int(monthly_sakes)
        return account

