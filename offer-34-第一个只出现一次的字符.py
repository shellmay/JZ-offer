# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        dic={}
        for i in s:
            if i in dic.keys():
                dic[i]=dic[i]+1
            else:
                dic[i]=1
        for i in range(len(list(s))):
            if dic[s[i]]==1:
                return i
        return -1
s=Solution()
end=s.FirstNotRepeatingChar('google')
print(end)