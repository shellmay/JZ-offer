# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        l=[]
        while listNode:
            l.append(listNode.val)
            listNode=listNode.next
        l.reverse()
        return l

n1=ListNode(1)
n2=ListNode(2)
n3=ListNode(3)
n1.next=n2
n2.next=n3
n=Solution()
end=n.printListFromTailToHead(n1)
print(end)