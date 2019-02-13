class point():
      def __init__(self,x=0,y=0):
          self.x = x
          self.y = y

      def str(self):
          p1 = point()
          print(p1)

      def add(self,other):
          sum = point()
          sum.x = self.x + other.x
          sum.y = self.y + other.y
          return sum

p1 = point(10,20)
p1.str()
p2 = point(20,30)
print(p1.add(p2).x,p1.add(p2).y)

