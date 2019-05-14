class BankAccount:

    interest_rate = float(1.00) 
    accounts = []

    def __init__(self):
        self.balance = 0

    def deposit(self, depo):
        self.balance += depo

    def withdraw(self, wdraw):
        self.balance -= wdraw
    
    @classmethod
    def create(cls):
        account_type = BankAccount()
        cls.accounts.append(account_type)
        return account_type
    
    @classmethod
    def total_funds(cls):
        total = 0
        for account in cls.accounts:
            total += account.balance
        return total
    
    @classmethod
    def interest_time(cls):
        for account in cls.accounts:
            account.balance += account.balance * (cls.interest_rate / 100)



my_account = BankAccount.create()
your_account = BankAccount.create()
print(my_account.balance) # 0
print(BankAccount.total_funds()) # 0
my_account.deposit(200)
your_account.deposit(1000)
print(my_account.balance) # 200
print(your_account.balance) # 1000
print(BankAccount.total_funds()) # 1200
BankAccount.interest_time()
print(my_account.balance) # 202.0
print(your_account.balance) # 1010.0
print(BankAccount.total_funds()) # 1212.0
my_account.withdraw(50)
print(my_account.balance) # 152.0
print(BankAccount.total_funds()) # 1162.0
    