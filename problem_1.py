#problem 1: Square Numbers and Return Their Sum

class Point:
  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z

  def Sqsum(self):
    a = self.x **2
    b = self.y **2
    c = self.z **2
    return(a+b+c)

num = Point(1,3,5)
num.Sqsum()
