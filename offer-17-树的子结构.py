# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        cur=root
        self.i(root)
        return cur

    def i(self,root):
        if root.right!=None and root.left!=None:
            root.left,root.right=root.right,root.left
            self.i(root.left)
            self.i(root.right)
        if root.right!=None and root.left==None:
            root.left,root.right=root.right,None
            self.i(root.left)
        if root.right==None and root.left!=None:
            root.left,root.right=None,root.left
            self.i(root.right)
        if root.right==None and root.left==None:
            return


