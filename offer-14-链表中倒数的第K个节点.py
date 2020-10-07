# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#两个指针距离k的单位，当前面的指针到达最后的一个结点时，说明前一个结点已经到达倒数第k个结点
class Solution:
    # 返回ListNode
    def FindKthToTail(self,head,k):
        #前后指针
        formar,latter=head,head
        #前指针先走k步
        for i in range(k):
            if formar:formar=formar.next
            else:return
        #同时走，直到前指针走完链表
        while formar:
            formar,latter=formar.next,latter.next
        return latter
