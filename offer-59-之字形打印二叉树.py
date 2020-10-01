# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        index=True
        end=[pRoot]
        en=[]
        while pRoot:
            tmp=[]
            index=not index
            for i in end:
                tmp.append(i.val)
                if i.left:
                    end.append(i.left)
                if i.right:
                    end.append(i.right)
            en.append(tmp[::-1] ) if index else en.append(tmp)
        return