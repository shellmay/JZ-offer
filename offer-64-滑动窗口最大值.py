# -*- coding:utf-8 -*-
class Solution:
    def maxInWindows(self, num, size):
        # write code here
        if len(num)<size or size<=0:
            return []

        max=[]
        for i in range(len(num)-size+1):
            max.append(sorted(num[i:i+size],reverse=True)[0])
        return max
s=Solution()
end=s.maxInWindows([2,3,4,2,6,2,5,1],3)
print(end)