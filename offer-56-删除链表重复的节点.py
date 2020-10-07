# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    #快慢指针
    def deleteDuplication(self, pHead):
        dummy=ListNode(-1)
        dummy.next=pHead
        low=dummy
        faster=pHead
        while faster:
            if faster.val==low.val:
                faster=faster.next
                low.next=faster
            else:
                low=low.next
                faster=faster.next
        return dummy.next
    #递归
    


