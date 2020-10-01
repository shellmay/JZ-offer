# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        cur=None
        if   pHead2!=None and pHead1!=None:
            if pHead1.val>pHead2.val:
                p = ListNode(pHead2.val)
                cur = p
                pHead2 = pHead2.next
            else:
                p = ListNode(pHead1.val)
                pHead1 = pHead1.next
                cur = p
        while pHead2!=None and pHead1!=None:
            if pHead2.val<pHead1.val:
                p.next=pHead2
                pHead2=pHead2.next
                p=p.next
            else:
                p.next = pHead1
                pHead1 = pHead1.next
                p=p.next
        if cur==None:
            if pHead1==None:
                return pHead2
            else:
                return pHead1
        if pHead2!=None and pHead1==None:
            while pHead2!=None:
                p.next=pHead2
                pHead2=pHead2.next
                p=p.next
        if pHead1!=None and pHead2==None:
            while pHead1!=None:
                p.next=pHead1
                pHead1=pHead1.next
                p=p.next
        return cur