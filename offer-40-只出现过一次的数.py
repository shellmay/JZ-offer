# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        dic={}
        di=[]
        for i in array:
            if i in dic.keys():
                dic[i]=dic[i]+1
            else:dic[i]=1
        for i ,value in dic.items():
            if value==1:
                di.append(i)
        return di

s=Solution()
end=s.FindNumsAppearOnce([2,4,3,6,3,2,5,5])
print(end)