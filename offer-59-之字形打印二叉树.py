# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#1、利用两个栈，先进后出的特点做这道题。
#2、一个栈顺着存，一个栈逆着存
#
#
class Solution:
    def Print(self, pRoot):
        if not pRoot:return []
        stack1=[pRoot]
        stack2=[]
        rsc=[]
        while (stack1 or stack2):
            r1=[]
            r2=[]
            while stack1:
                cur=stack1.pop()
                r1.append(cur.val)
                if cur.left:
                    stack2.append(cur.left)
                if cur.right:
                    stack2.append(cur.right)
            if len(r1)!=0:
                rsc.append(r1)
            while stack2:
                cur=stack2.pop()
                r2.append(cur.val)
                if cur.right:
                    stack1.append(cur.right)
                if cur.left:
                    stack1.append(cur.left)
            if len(r2)!=0:
                rsc.append(r2)
        return rsc
