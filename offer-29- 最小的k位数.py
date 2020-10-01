# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if tinput and k>0 and k<=len(tinput):
            tinput=sorted(tinput)
            return tinput[:k]
        else:
            return []
ss=Solution()
end=ss.GetLeastNumbers_Solution([4,5,1,6,2,7,3,8],10)
print(end)