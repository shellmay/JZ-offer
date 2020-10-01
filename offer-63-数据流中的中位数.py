# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.number=[]
    def Insert(self, num):
        # write code here
        self.number.append(num)
    def GetMedian(self,fuck):
        # write code here
        self.number.sort()
        n=len(self.number)
        if n%2!=0:
            return self.number[n//2]
        else:
            return (self.number[n//2]+self.number[n//2-1])/2.0

from heapq import *

class Solution:
    def __init__(self):
        self.A = [] # 小顶堆，保存较大的一半
        self.B = [] # 大顶堆，保存较小的一半

    def Insert(self, num) :
        if len(self.A) != len(self.B):
            heappush(self.B, -heappushpop(self.A, num))
        else:
            heappush(self.A, -heappushpop(self.B, -num))

    def GetMedian(self) :
        return self.A[0] if len(self.A) != len(self.B) else (self.A[0] - self.B[0]) / 2.0


