# -*- coding:utf-8 -*-
class Solution:
    # 返回对应char
    def __init__(self):
        self.s = ''
        self.dict = {}
    def FirstAppearingOnce(self):
        # write code here
        for i in self.s:
            if self.dict[i]==1:
                return i
        return "#"
    def Insert(self, char):
        # write code here
        self.s += char
        self.dict[char]=self.dict.get(char,0)+1
s=Solution()
s.Insert('g')
print(s.FirstAppearingOnce())
s.Insert('0')
print(s.FirstAppearingOnce())
s.Insert('0')
print(s.FirstAppearingOnce())
s.Insert('g')
print(s.FirstAppearingOnce())
s.Insert('l')
print(s.FirstAppearingOnce())
s.Insert('e')
print(s.FirstAppearingOnce())