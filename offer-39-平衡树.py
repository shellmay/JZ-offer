# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        if pRoot==None:
            return True
        if pRoot.left==None and  pRoot.right==None:
            return True
        def deep(p):
            if not p:
                return 0
            return 1+max(deep(p.left),deep(p.right))

        return abs(deep(pRoot.left)-deep(pRoot.right))<=1 and pRoot.left and pRoot.right