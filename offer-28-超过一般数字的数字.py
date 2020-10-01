# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        num_set=list(set(numbers))
        for i in num_set:
            if numbers.count(i)>len(numbers)//2:
                return i
        return 0
s=Solution()
end=s.MoreThanHalfNum_Solution([1,2,3,2,2,2,5,4,2])
print(end)
