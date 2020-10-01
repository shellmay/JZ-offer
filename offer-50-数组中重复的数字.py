# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        if numbers==None and len(numbers)==0:
            return False
        for i in numbers:
            if i <0 or i>len(numbers):
                return False
        f_arr=[False]*len(numbers)
        for i in range(len(numbers)):
            if f_arr[numbers[i]]==True:
                duplication[0]=numbers[i]
                return True
            f_arr[numbers[i]]=True
        return False

a=[2,1,3,1,4]
b=[]
s=Solution()
print(s.duplicate(a,b))