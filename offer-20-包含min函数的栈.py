# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.m,self.a=[],[]

    def push(self, node):
        self.a.append(node)
        if self.m==[] or self.m[-1]>=node:
            self.m.append(node)
        print(self.a,self.m)

    # write code here
    def pop(self):
        if self.a.pop()==self.m[-1]:
            self.m.pop()
        print(self.a, self.m)

    # write code here
    def top(self):
        return self.a[-1]

    # write code here
    def min(self):
        return self.m[-1]
# write code here
test = Solution()
test.push(3)
print(test.min())
test.push(4)
print(test.min())
test.push(2)
print(test.min())
test.push(3)
print(test.min())
test.pop()
print(test.min())
test.pop()
print(test.min())
test.pop()
print(test.min())
test.push(0)
print(test.min())


