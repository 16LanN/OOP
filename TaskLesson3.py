from datetime import datetime
class Amount:
    def __init__(self, amount, transaction_type):
        self.__amount = amount
        self.__timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.__transaction_type = transaction_type
        
    def __str__(self):
        return f"""-------------------------
Amount: {self.__amount} 
Timestamp: {self.__timestamp} 
Type: {self.__transaction_type}
-------------------------"""

class PersonalAccount:
    def __init__(self, account_number, account_holder, balance):
        self.__account_number = account_number
        self.__owner_name = account_holder
        self.__balance = balance
        self.__transactions = []

    def deposit(self, amount):
        self.__balance += amount
        transaction = Amount(amount, "DEPOSIT")
        self.__transactions.append(transaction)

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            transaction = Amount(amount, "WITHDRAW")
            self.__transactions.append(transaction)
        else:
            print("Insufficient funds")
    
    def print_transaction_history(self):
        for transaction in self.__transactions:
            print(transaction)
        
    def get_balance(self):
        return self.__balance
    
    def get_account_number(self):
        return self.__account_number
    
    def set_account_number(self, new_account_number):
        self.__account_number = new_account_number

    def get_account_holder(self):
        return self.__owner_name 
    
    def set_account_holder(self, new_owner_name):
        self.__owner_name = new_owner_name

    def __str__(self):
        return f"""-------------------------
Account Number: {self.__account_number} 
Owner: {self.__owner_name}
Balance: {self.__balance}
-------------------------"""
    
    def __add__(self, amount):
        if isinstance(amount, (int, float)):
            self.deposit(amount)
            return self
        raise ValueError("Can only add numeric values to the account balance")
    
    def __sub__(self, amount):
        if isinstance(amount, (int, float)):
            self.withdraw(amount)
            return self
        raise ValueError("Can only subtract numeric values from the account balance")
    
p1 = PersonalAccount("123456789", "Alice", 1000)
p1 - 150
p1 + 900
print(p1.get_balance())
p1.print_transaction_history()
