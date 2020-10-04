# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    #自顶向下先序遍历求子树的深度
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
    #自底向上后序遍历求字数高度
    def isBalanced(self, root):
        def recur(root):
            if not root:return 0
            left=recur(root.left)
            if left==-1:return -1
            right=recur(root.right)
            if right==-1:return -1
            return 1+max(left,right) if abs(left-right)<=1 else -1
        return recur(root)!=-1
