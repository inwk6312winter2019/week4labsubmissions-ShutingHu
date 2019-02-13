

import math as m
class Point(object):
      def __init__(self,x = 0, y= 0):
          self.x = x
          self.y = y
      def distance_between_points(self,other):
          distance = 0.0
          distance =m.sqrt((self.x-other.x)**2 + (other.y-othr.y)**2)
          return distance
      def __add__(self,other):
         if isinstance(other,Point):
            return self.add_points(other)
         else:
            return self.increment(other)
      def add_points(self,other):
          sum = Point()
          sum.x = self.x + other.x
          sum.y = self.y + other.y
          return sum
      def increment(self,other):
          sum = Point()
          sum.x = self.x + other[0]
          sum.y = self.y + other[0]
          return sum
      def __radd__(self,other):
          return self.__add__(other)
      def print_point(self):
          print(self.x,self.y)
      def __str__(self):
         return ('(%d,%d)'%(self.x,self.y))


point1 = Point(10,20)
point2 = Point(15,25)
add = (20,30)
print( point1 + point2)
sum2 = point1 + add
sum3 = add + point1
print(sum2)
print(add + point1)
