# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        # write code here

        if not pHead:
            return pHead
        head=ListNode(-1)
        p=head
        p.next=pHead
        cur=pHead
        while cur and cur.next:
            if cur.val!=cur.next.val:
                cur=cur.next
                p=p.next
            else:
                val=cur.val
                while cur and cur.val==val:
                    cur=cur.next
                p.next=cur
        return head.next




        return pHead


