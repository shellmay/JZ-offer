# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        l=[]
        r=[]
        for i in array:
            if i%2==0:
                r.append(i)
            else:
                l.append(i)
        l.extend(r)
        return l