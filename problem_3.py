#problem3: Implement the Complete Student Class

class Student:
  def __init__(self, Name = 'Raj', RollNumber = 10):
    self._Name = Name
    self._RollNumber = RollNumber

  def getName(self):
    return self._Name

  def setName(self,x):
    self._Name = x

  def getRollNumber(self):
    return self._RollNumber

  def setRollNumber(self,y):
    self._RollNumber = y

obj  = Student()
obj.setName('Pankaj')
obj.getName()
obj.setRollNumber(2)
obj.getRollNumber()
