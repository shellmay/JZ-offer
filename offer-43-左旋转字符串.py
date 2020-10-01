# -*- coding:utf-8 -*-
class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        s=(s+s[:n])[n:]
        return s
s=Solution()
s.LeftRotateString('abcdf',2)