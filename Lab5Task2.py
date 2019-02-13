import copy as c
class point():
      def _init_(self):
          self.x = 0
          self.y = 0

class Rectangle():
      def _init_(self,width,height):
          self.width = 0
          self.height = 0
          self.concer = 0


def find_center(rect):
    p = point()
    p.x = rect.concer.x + rect.width/2
    p.y = rect.concer.y + rect.height/2
    return p

def print_point(p):
    print('the point is (%g,%g)' %(p.x,p.y))


def move_rectangle(rect,dx,dy):
    rect.concer.x += dx
    rect.concer.y += dy
    return rect.concer

def move_new_rectangle(rect,dx,dy):
    newbox = c.deepcopy(rect)
    newbox.concer.x += dx
    newbox.concer.y += dy
    return newbox.concer

box = Rectangle()
box.width = 100
box.height = 200
box.concer = point()
box.concer.x = 1
box.concer.y = 1

print('the rectangle leftconcer is (%g,%g) and the width is %g,the height is %g' %(box.concer.x,box.concer.y,box.width,box.height))
print_point(move_rectangle(box,10,15))
print_point(move_new_rectangle(box,10,15))
