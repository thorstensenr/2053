from bank_account import BankAccount

account = BankAccount('091234', 100.00)
account.deposit(50)
print(account.get_balance())
account.withdraw(25)
print(account.get_balance())
print(account)