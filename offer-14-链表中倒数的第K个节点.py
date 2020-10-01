# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        last=None
        cur=pHead
        if pHead==None:
            return pHead
        else:
            while cur!=None:
                temp = cur.next
                cur.next = last
                last = cur
                cur = temp

            return last
