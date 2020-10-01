# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if not root:
            return []
        res=[]
        head=root
        qu=[]
        qu.append([head,expectNumber-head.val,[head.val]])
        while qu:
            head,expectNumber,list_node=qu.pop()
            if expectNumber==0 and head.left==None and head.right==None:
                res.append(list_node)
            if head.right:
                qu.append([head.right,expectNumber-head.right.val,list_node+[head.right.val]])
            if head.left:
                qu.append([head.left,expectNumber-head.left.val,list_node+[head.left.val]])

        return res