class Kangaroo(object):
      def __init__(self,name,pouch_contents = []):
          self.pouch_contents = pouch_contents
          self.name = name
      def put_in_pouch(self,item):
          self.pouch_contents.append(item)
          print(self.pouch_contents)
      def __str__(self):
          t = [self.name + 'has pouch contents:']
          for obj in self.pouch_contents:

kanga = Kangaroo('Kanga')
roo = Kangaroo('Roo')
kanga.put_in_pouch('apple')
kanga.put_in_pouch('banana')
kanga.put_in_pouch(roo)

print(kanga)
print(roo)

