class Person():
    def __init__(self, name: str, second_name: str, age: int, cpf: str):
        self._name = name
        self._second_name = second_name
        self._age = age
        self._cpf = cpf
        self._accounts = []

    def info_person(self):
        return (
            f"Name: {self._name}\n"
            f"Second Name: {self._second_name}\n"
            f"Age: {self._age}\n"
            f"CPF: {self._cpf}\n"
            f"Accounts: {self._accounts}\n"
        )
    
    def info_accounts(self):
        if not self._accounts:
            return "No accounts found."
        return "\n".join(account.info_account() for account in self._accounts)
    
    def add_account(self, account):
        if account not in self._accounts:
            self._accounts.append(account)

    @property    
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def second_name(self):
        return self._second_name

    @second_name.setter
    def second_name(self, value):
        self._second_name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, value):
        self._cpf = value

    @property
    def accounts(self):
        return self._accounts

    @classmethod
    def from_input(cls):
        print("Register a new person:")
        name = input("Name: ").strip()
        second_name = input("Second Name: ").strip()
        age = int(input("Age: "))
        cpf = input("CPF: ").strip()
        return cls(name, second_name, age, cpf)
    
    def to_csv_row(self):
        return [self._name, self._second_name, str(self._age), self._cpf]
    
    @classmethod
    def from_csv_row(cls, row):
        name, second_name, age, cpf = row
        return cls(name, second_name, int(age), cpf)
