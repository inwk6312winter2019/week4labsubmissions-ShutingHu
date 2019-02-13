import math as m
def distance_between_points(p1,p2):
    distance = 0.0
    distance = m.sqrt((p1.x-p2.x) ** 2 + (p1.y-p2.y) ** 2)
    print('the distance between (%g,%g) and (%g,%g) is %g' %(p1.x,p1.y,p2.x,p2.y,distance))

class point():
      def __int__(self):
          self.x = 0
          self.y = 0
      def __str__(self):
          return '(%d,%d)' %(self.x,self.y)
      def __add__(self,other):
          sum = point()
          sum.x = self.x + other.x
          sum.y = self.y + other.y 
          return sum   


point1 = point()
point1.x = 6
point1.y = 5

point2 = point()
point2.x = 3
point2.y = 1

distance_between_points(point1,point2)
print(point1)
print(point1 + point2)
