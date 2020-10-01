# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        # write code here
        s=list(s.split(' '))
        s.reverse()
        return ' '.join(s)
s=Solution()
end=s.ReverseSentence('student. a am I')
print(end)