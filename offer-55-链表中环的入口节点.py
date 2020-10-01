# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        a=[]
        while pHead:
            if pHead  in a:
                return pHead
            else:
                a.append(pHead)
            pHead=pHead.next

