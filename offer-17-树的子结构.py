# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        def issutree(p1,p2):
            if not p2:
                return True
            if not p1 or p1.val != p2.val:
                return False
            return issutree(p1.left,p2.left) and issutree(p1.right,p2.right)
        return bool(pRoot1 and pRoot2) and (issutree(pRoot1,pRoot2) or self.HasSubtree(pRoot1.left,pRoot2) or self.HasSubtree(pRoot1.right,pRoot2))
