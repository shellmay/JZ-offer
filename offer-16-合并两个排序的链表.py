# -*- coding:utf-8 -*-
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None
#直接循环和递归
class Solution:
     #直接循环
    def Merge(self, pHead1, pHead2):
        #伪造一个头结点
        merge=cur=ListNode(0)
        #当都存在时，小的作为下一个结点
        while pHead1 and pHead2:
            if pHead1.val<pHead2.val:
                cur.next=pHead1
                pHead1=pHead1.next
            else:
                cur.next=pHead2
                pHead2=pHead2.next
            cur=cur.next
        #当有一个链表为空时，下一个就是剩下的链表
        cur.next=pHead1 if pHead1 else pHead2
        #注意返回头结点是伪头结点的下一个结点
        return merge.next
    
    
    #递归
    #递归时判断小的值，递归回溯时从后往前接入链表
    def Merge(self, pHead1, pHead2):
        if not pHead1:return pHead2
        if not pHead2:return pHead1
        if pHead1.val<pHead2.val:
            pHead1.next=self.Merge(pHead1.next,pHead2)
            return pHead1
        pHead2.next=self.Merge(pHead1,pHead2.next)
        return pHead2
