class Bank():
    def __init__(self, name: str, cnpj: str, number: int):
        self._name = name
        self._cnpj = cnpj
        self._number = number
        self._accounts = []


    def info_bank(self):
        return (
        f"Bank Name: {self._name}\n"
        f"CNPJ: {self._cnpj}\n"
        f"Number: {self._number}\n" 
        f"Accounts: {len(self._accounts)} total\n" 
        )
    
    def add_account(self, account):
        if account not in self._accounts:
            self._accounts.append(account)

    def delete_account(self, account):
        if account in self._accounts:
            self._accounts.remove(account)
        else:
            print("Account not found in the bank.")

    def list_accounts(self):
        if not self._accounts:
            return "No accounts in this bank."
        return "\n".join(account.info_account() for account in self._accounts)
        
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def cnpj(self):
        return self._cnpj

    @cnpj.setter
    def cnpj(self, value):
        self._cnpj = value

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        self._number = value

    @property
    def accounts(self):
        return self._accounts

    @classmethod
    def from_input(cls):
        print("Registering a new bank:")
        name = input("Bank Name: ").strip()
        cnpj = input("CNPJ: ").strip()
        number = int(input("Bank Number: "))
        return cls(name, cnpj, number)

    def to_csv_row(self):
        return [self._name, self._cnpj, str(self._number)]
    
    @classmethod
    def from_csv_row(cls, row):
        name, cnpj, number = row
        return cls(name, cnpj, int(number))