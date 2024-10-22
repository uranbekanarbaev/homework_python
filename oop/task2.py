
class BankAccount:
    def __init__(self, account_num, name, balance):
        self.account_num = account_num
        self.name = name
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def check_balance(self):
        return self.balance

class BankSystem:
    def __init__(self):
        self.bank_accounts = []
    
    def add_account(self, bank_account: BankAccount):
        self.bank_accounts.append(bank_account)

    def transfer(self, sender_number, receiver_number, amount):
        for bank_account in self.bank_accounts:
            sender = None
            receiver = None
            if sender_number == bank_account.name:
                sender = bank_account
            elif receiver_number == bank_account.name:
                receiver = bank_account
        
        if sender and receiver:
            sender.withdraw(amount)
            receiver.deposit(amount)
        else:
            return "Wrong information about sender or receiver"

# Пример использования
account1 = BankAccount("12345", "Иван Иванов", 1000)
account2 = BankAccount("67890", "Петр Петров", 2000)
bank = BankSystem()
bank.add_account(account1)
bank.add_account(account2)
account1.deposit(500)
account2.withdraw(300)
bank.transfer("12345", "67890", 200)
print(account1)
print(account2)
