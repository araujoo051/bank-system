from abc import ABC, abstractmethod
from models.person import Person
from models.bank import Bank

class BankAccount(ABC):
    def __init__(self, holder: Person, bank: Bank, number: int, balance: float = 0.0, password: str=""):
        self._holder = holder
        self._bank = bank
        self._number = number
        self._balance = balance
        self._password = password

    @abstractmethod
    def withdraw(self, amount: float):
        pass

    def deposit(self, amount: float):
        if amount > 0:
            self._balance += amount
            return f"Deposit successful. New balance: {self._balance}"
        else:
            return "Invalid deposit amount."
    
    def verify_password(self, pwd: str) -> bool:
        return self._password == pwd
    
    def info_account(self):
        return (
            f"Account Number: {self._number}\n"
            f"Holder: {self._holder.name} {self._holder.second_name}\n"
            f"Bank: {self._bank.name}\n"
            f"Balance: {self._balance}\n"
        )
    
    @property
    def holder(self):
        return self._holder

    @holder.setter
    def holder(self, value):
        self._holder = value

    @property
    def bank(self):
        return self._bank
    
    @bank.setter
    def bank(self, value):
        self._bank = value
    
    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        self._number = value

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        self._balance = value

    @property
    def password(self):
        return "****" 

    @password.setter
    def password(self, value):
        self._password = value
