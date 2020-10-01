# -*- coding:utf-8 -*-
class TreeNode:
     def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if len(pre)>0:
            father = TreeNode(pre[0])
            father_id=tin.index(pre[0])
            father.left=self.reConstructBinaryTree( pre[1:1+father_id], tin[:father_id])
            father.right=self.reConstructBinaryTree(pre[father_id+1:],tin[father_id+1:])
            return father

a=[1,2,4,7,3,5,6,8]
b=[4,7,2,1,5,3,8,6]
c=Solution()
v=c.reConstructBinaryTree(a,b)
print(v.left.left.val)

