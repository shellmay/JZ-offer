# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#解题思路：
#1、当左右子树都已经过了叶子节点，则对称
#2、当左右有一边不存在时或者是两边不相等时，则不对称
#3、递归判断左子树的左子树和右子树的右子树，左子树的右子树和右子树的左子树是否对称，回溯判断是否都满足。（自顶向下）
class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        def bu(l,r):
            if not l and not r:return True
            if not l or not r or l.val!=r.val:return False
            return bu(l.left,r.right) and bu(l.right,r.left)
        return bu(pRoot.left,pRoot.right) if pRoot else True
