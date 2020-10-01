# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
# write code here
        cur_num=array[0]
        max_num=[array[0]]
        for a in array[1:]:
            cur_num=max(cur_num+a,a)
            max_num.append(cur_num)
        return max(max_num)

s=Solution()
end=s.FindGreatestSumOfSubArray([6,-3,-2,7,-15,1,2,2])
print(end)
