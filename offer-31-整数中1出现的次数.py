# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        str1=''
        for i in range(n+1):
            str1+=str(i)
        list1=list(str1)
        return list1.count('1')
s=Solution()
end=s.NumberOf1Between1AndN_Solution(200)
print(end)