# -*- coding:utf-8 -*-
class RandomListNode:
    def __init__(self, x):
       self.label = x
       self.next = None
       self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if not pHead:
            return pHead
        cloNode = pHead
        while cloNode:
            node = RandomListNode(cloNode.label)
            node.next = cloNode.next
            cloNode.next = node
            cloNode = node.next
        cloNode = pHead
        while cloNode:
            node = cloNode.next
            if cloNode.random:
                node.random = cloNode.random.next
            cloNode = node.next
        cloNode = pHead
        pHead = pHead.next
        while cloNode.next:
            node = cloNode.next
            cloNode.next = node.next
            cloNode = node
        return pHead
l=RandomListNode(1)
l2=RandomListNode(2)
l3=RandomListNode(3)
l.next=l2
l.random=l3
l2.next=l3
l2.random=l

s=Solution()
print(s.Clone(l))


