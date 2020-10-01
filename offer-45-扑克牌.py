# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if not numbers:
            return False
        numbers.sort()
        joker=numbers.count(0)
        for i in range(4):
            if numbers[i]==0:
                continue
            elif numbers[i]==numbers[i+1]:
                return False
        return numbers[-1]-numbers[joker]<5
