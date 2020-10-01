# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        a=[0,1,1]
        if n==0:
            return 0
        elif n==1 or n==2:
            return 1
        else:
            k=2
            while k<n:
                a.append(a[k]+a[k-1])
                k+=1
            return a.pop()

s=Solution()
a=s.Fibonacci(39)
print(a)