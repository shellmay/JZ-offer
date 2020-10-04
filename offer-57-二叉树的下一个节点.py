# -*- coding:utf-8 -*-
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
#两种情况：
#1、当该结点的右子树存在时，寻找右子树的最左边的左子树，否则就是右子树
#2、当该结点的右子树不存在时，寻找第一个以该子树为左子树的根
class Solution:
    def GetNext(self, pNode):
        # write code here
        if not pNode:
            return pNode
        if pNode.right:
            pNode=pNode.right
            while pNode.left:
                pNode=pNode.left
            return pNode
        else:
            while pNode.next:
                if pNode==pNode.next.left:
                    return pNode.next
                pNode=pNode.next
            return None
