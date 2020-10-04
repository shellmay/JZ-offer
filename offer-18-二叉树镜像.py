# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if root==None:
            return
        #不断地交换左右子树即可
        root.left,root.right=root.right,root.left
        self.Mirror(root.left)
        self.Mirror(root.right)
node=TreeNode(1)
node.left=TreeNode(2)
node.right=TreeNode(3)
node.left.left=TreeNode(4)
node.left.right=TreeNode(5)
s=Solution()
s.Mirror(node)
print(node.right.left.val)
