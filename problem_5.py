#problem 5: Handling a Bank Account

class Account:
  def __init__(self, title=None, balance=0):
    self.title = title
    self.balance = balance

  def withdrawal(self, amount):
    if self.balance >= amount:
      self.balance -= amount
    else:
      print("Insufficient funds")

  def deposit(self, amount):
    self.balance += amount

  def getBalance(self):
    return self.balance

class SavingsAccount(Account):
  def __init__(self,title, balance, interestRate):
    super().__init__(title,balance)
    self.interestRate = interestRate

  def interestAmount(self):
    return (self.interestRate * self.balance)//100

account = Account("Ashish", 2000)
account.deposit(500)
account.getBalance()
account.withdrawal(500)
account.getBalance()
saccount = SavingsAccount("Ashish", 2000, 5)
saccount.interestAmount()