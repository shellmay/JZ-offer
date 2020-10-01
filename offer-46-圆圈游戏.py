# -*- coding:utf-8 -*-
class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        end=0
        for i in range(1,n+1):
            end=(n+i)%m
        return end
s=Solution()
end=s.LastRemaining_Solution(5,3)
print(end)