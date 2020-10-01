# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isSymmetrical(self, pRoot):
        # write code here

        def bu(l,r):
            if not l and not r:return True
            if not l or not r or l.val!=r.val:return False
            return bu(l.left,r.right) and bu(l.right,r.left)
        return bu(pRoot.left,pRoot.right) if pRoot else True