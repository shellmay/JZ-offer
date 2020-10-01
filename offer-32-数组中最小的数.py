# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if not numbers: return ''
        numbers=list(sorted(numbers))
        numbers=[str(i) for i in numbers]
        res=[]
        def helper(numbers,tmp):
            if not numbers: res.append(int(''.join(tmp)))
            for i,char in enumerate(numbers):
                if i>0 and numbers[i]==numbers[i-1]:
                    continue
                helper(numbers[:i]+numbers[i+1:],tmp+[char])
        helper(numbers,[])
        return min(res)


s=Solution()
end=s.PrintMinNumber([3,32,321])
print(end)
