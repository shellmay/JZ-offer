# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        f=[0,1,2]
        if number==1:
            return 1
        elif number==2:
            return 2
        elif number==0:
            return 0
        else:
            for i in range(2,number):
                f.append(f[i]+f[i-1])
            return f.pop()
s=Solution()
end=s.rectCover(10)
print(end)