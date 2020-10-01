# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        node1, node2 = pHead1, pHead2

        while node1 != node2:
            node1 = node1.next if node1 else pHead2
            node2 = node2.next if node2 else pHead1

        return node1

