# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.a=[]
        self.b=[]
    def push(self, node):
        # write code here
       self.a.append(node)
    def pop(self):
        # return xx
       if self.a==None:
           return None
       else:
           for i in range(len(self.a)):
               self.b.append(self.a.pop())
           end = self.b.pop()
           for i in range(len(self.b)):
               self.a.append(self.b.pop())
           return end
s=Solution()
s.push(1)
s.push(2)
s.push(3)
print(s.pop())
print(s.pop())
s.push(4)
print(s.pop())
s.push(5)
print(s.pop())
print(s.pop())

