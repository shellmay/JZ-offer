# -*- coding:utf-8 -*-
class Solution:
    def Add(self, num1, num2):
    # write code here
        if num1 is None or num2 is None:
            return -1

        while num2 != 0:
            sums = num1 ^ num2
            num2 = (num1&num2)<<1 # 进位
            num1 = sums & 0xFFFFFFFF # 考虑负数
        return num1 if num1 >> 31 == 0 else num1 - 4294967296