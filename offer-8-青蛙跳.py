# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        step=[1,2]
        if number==1:
            return step[0]
        elif number==2:
            return step[1]
        else:
            for i in range(2,number):
                step.append(step[i-1]+step[i-2])
            return step.pop()
s=Solution()
end=s.jumpFloor(5)
print(end)


