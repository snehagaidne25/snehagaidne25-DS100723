#problem 4: Implement a Banking Account

class Account:
  def __init__(self, title , balance):
    self.title = title
    self.balance = balance

    # write your code here

class SavingsAccount(Account):
  def __init__(self,title, balance, interestRate):
    super().__init__(title,balance)
    self.interestRate = interestRate

account = Account("Ashish", 5000)
SAccount = SavingsAccount("Ashish", 5000, 5)
account.title
account.balance
SAccount.interestRate
