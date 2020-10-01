# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        a=-1
        b=-1
        for i in array:
            if tsum-i in array:
                if a==-1 and b==-1:
                    a, b = i, tsum - i
                elif i * (tsum - i) < a * b:
                    a, b = i, tsum - i
        if  a!=-1 and b!=-1:
            return [a,b]
        else:return []
s=Solution()
end=s.FindNumbersWithSum([1,2,4,7,11,15],15)
print(end)