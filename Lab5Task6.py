
class point:
      def __init__(self,x=0,y=0):
          self.x = x
          self.y = y

      def str(self):
          p1 = point()
          print(p1)

      def add(self,other):
          sum = point()
          if type(other) is tuple:
             sum.x = self.x + t[0]
             sum.y = self.y + t[1]
          elif isinstance(other,point):
             sum.x = self.x + other.x
             sum.y = self.y + other.y
          return sum


p1 = point(10,20)
p1.str()
p2 = point(20,30)
print(p1.add(p2).x,p1.add(p2).y)
t = (15,20)
print(p1.add(t).x,p1.add(t).y)
