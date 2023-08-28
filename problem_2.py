#problem 2: Implement a Calculator Class

class Calculator:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def add(self):
    add = self.x + self.y
    return add

  def subtract(self):
    sub = self.y - self.x
    return sub

  def multiply(self):
    mul = self.x * self.y
    return mul

  def divide(self):
    div = self.y / self.x
    return div

obj = Calculator(10,94)
obj.add()
obj.subtract()
obj.multiply()
obj.divide()
