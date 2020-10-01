# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        if  n<0:
            n=n&(0xffffffff)
        return bin(n).count('1')