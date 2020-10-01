# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        a=[2,3,5]
        if index==1 :
            return [index]
        if index==0:
            return []
        l=[1]
        def ugly(number):
            if number==0 or number==1:
                return True
            for i in a:
                if number%i==0:
                    print(number)
                    ugly(number/i)
            return False
        for i in range(2,index):
            print(i)
            if ugly(i):
                l.append(i)
        return l


s=Solution()
end=s.GetUglyNumber_Solution(100)
print(end)