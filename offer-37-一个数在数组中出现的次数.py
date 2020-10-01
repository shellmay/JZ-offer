# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        end=0
        for i in data:
            if i==k:
                end+=1
        return  end

