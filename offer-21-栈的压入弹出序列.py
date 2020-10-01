# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        a=[]
        while popV:
            tmp=popV.pop(0)
            if tmp in pushV:
                a.extend(pushV[:pushV.index(tmp)])
                pushV=pushV[pushV.index(tmp)+1:]
            else:
                if a==[]:
                    break
                if a[-1]==tmp:
                    a.pop()
                else:
                    break
        if popV==[] and pushV==[]:
            return True
        else:
            return False
s=Solution()
end=s.IsPopOrder([1],[2])
print(end)
