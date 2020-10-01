# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        index=tsum//2+1
        i=1
        k=2
        res=[]
        while k<=index:
            if sum(list(range(i,k+1)))<tsum:
                k+=1
            elif sum(list(range(i,k+1)))>tsum:
                i+=1
            else:
                res.append(list(range(i,k+1)))
                k+=1
        return res
s=Solution()
end=s.FindContinuousSequence(100)
print(end)