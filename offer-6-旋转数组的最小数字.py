# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if len(rotateArray)==1:
            return rotateArray[0]
        else:
            temp = rotateArray[0]
            for i in rotateArray[1:]:
                if i < temp:
                    end = i
                    break
            return end

a=[4,5,6,2,3]
s=Solution()
end=s.minNumberInRotateArray(a)
print(end)