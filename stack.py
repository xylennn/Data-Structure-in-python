class stack():
      def __init__(self):
          self.item=[]
      def push(self,data):
          return self.item.append(data)
      def pop(self):
          return self.item.pop()
      def get_stack(self):
          return self.item
      def is_empty(self):
          return self.item == []
      def peak(self):
          return self.item[-1]

s= stack()
s.push('a')
s.push('b')
s.push('c')
s.push('d')
s.pop()
s.get_stack()
s.is_empty()
s.peak()
