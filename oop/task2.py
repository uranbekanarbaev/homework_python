"""
Задача 2: Создание банковской системы
Создайте систему для управления банковскими счетами. У каждого счета должны быть атрибуты: номер счета, имя владельца, баланс. Система должна поддерживать следующие операции:

1. Депозит средств.
2. Снятие средств.
3. Проверка баланса.
4. Перевод средств с одного счета на другой.

Используйте магические методы для вывода информации о счете и для проверки равенства счетов (например, по номеру счета).
"""

class BankAccount:
    """
    A class to represent a bank account.

    Attributes:
        account_num (int): The account number of the bank account.
        name (str): The name of the account holder.
        balance (float): The current balance of the account.
    """

    def __init__(self, account_num: int = None, name: str = None, balance: float = 0):
        """
        Initializes a new BankAccount instance.

        Args:
            account_num (int): The account number.
            name (str): The name of the account holder.
            balance (float): The initial balance of the account.
        """
        self.account_num = account_num
        self.name = name
        self.balance = balance
    
    def deposit(self, amount: float = 0):
        """
        Deposits a specified amount into the bank account.

        Args:
            amount (float): The amount to be deposited.
        """
        self.balance += amount

    def withdraw(self, amount: float = 0):
        """
        Withdraws a specified amount from the bank account.

        Args:
            amount (float): The amount to be withdrawn.
        """
        if self.check_balance() >= amount:
            self.balance -= amount
        else:
            raise ValueError

    def check_balance(self):
        """
        Checks the current balance of the bank account.

        Returns:
            float: The current balance of the account.
        """
        return self.balance


class BankSystem:
    """
    A class to represent a banking system managing multiple accounts.

    Attributes:
        bank_accounts (list): A list of BankAccount instances.
    """

    def __init__(self):
        """
        Initializes a new BankSystem instance with an empty account list.
        """
        self.bank_accounts = []
    
    def add_account(self, bank_account: BankAccount = None):
        """
        Adds a BankAccount instance to the banking system.

        Args:
            bank_account (BankAccount): The bank account to be added.
        """
        self.bank_accounts.append(bank_account)

    def transfer(self, sender_number: int = None, receiver_number: int = None, amount: float = 0):
        """
        Transfers a specified amount from one account to another.

        Args:
            sender_number (str): The account number of the sender.
            receiver_number (str): The account number of the receiver.
            amount (float): The amount to transfer.

        Returns:
            str: A message indicating success or failure of the transfer.
        """
        sender = None
        receiver = None

        # Using a single pass to find both accounts
        for bank_account in self.bank_accounts:
            if sender_number == bank_account.account_num:
                sender = bank_account
            elif receiver_number == bank_account.account_num:
                receiver = bank_account

        if sender is None:
            raise Exception("Sender bank account is not found")
        if receiver is None:
            raise Exception("Receiver bank account is not found")

        try:
            sender.withdraw(amount)
            receiver.deposit(amount)
            return "Transfer successful"
        except Exception as e:
            return str(e)  # Return the exception message if withdrawal fails

# Пример использования

if __name__ == '__main__':
    account1 = BankAccount("12345", "Ivan Ivanov", 1000)
    account2 = BankAccount("67890", "Petr Petrov", 2000)
    bank = BankSystem()
    bank.add_account(account1)
    bank.add_account(account2)
    account1.deposit(500)
    account2.withdraw(300)
    transfer_message = bank.transfer("12345", "67890", 200)
    print(transfer_message)
    print(f"Account 1 balance: {account1.check_balance()}")
    print(f"Account 2 balance: {account2.check_balance()}")
