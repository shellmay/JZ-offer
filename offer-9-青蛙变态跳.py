# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        # write code here
        return 2**(number-1)
s=Solution()
end=s.jumpFloorII(39)
print(end)


