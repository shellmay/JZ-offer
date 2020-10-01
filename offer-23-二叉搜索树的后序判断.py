# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if not sequence:return False
        return self.if_tree(sequence)
    def if_tree(self,s):
        if not s:return True
        root=s[-1]
        index=0
        for i in range(len(s)):
            if s[i]>=root:
                index=i
                break
        left=s[:index]
        right=s[index:-1]
        for i in right:
            if i<root:
                return False
        return self.if_tree(left) and self.if_tree(right)

a=[1,6,3,2,5]
s=Solution()
print(s.VerifySquenceOfBST(a))