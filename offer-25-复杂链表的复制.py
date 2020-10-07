# -*- coding:utf-8 -*-
"""
从头结点 head 开始拷贝；
由于一个结点可能被多个指针指到，因此如果该结点已被拷贝，则不需要重复拷贝；
如果还没拷贝该结点，则创建一个新的结点进行拷贝，并将拷贝过的结点保存在哈希表中；
使用递归拷贝所有的 next 结点，再递归拷贝所有的 random 结点。
"""
class RandomListNode:
    def __init__(self, x):
       self.label = x
       self.next = None
       self.random = None
class Solution:
    #深度遍历
    def Clone(self,pHead):
        def dfs(pHead):
            if not pHead: return None
            #是否已经遍历过
            if pHead in visited:
                return visited[pHead]
            # 创建新结点
            copy = RandomListNode(pHead.label)
            #加入遍历集合
            visited[pHead] = copy
            copy.next = dfs(pHead.next)
            copy.random = dfs(pHead.random)
            return copy
        visited = {}
        return dfs(pHead)
    
    
    
l=RandomListNode(1)
l2=RandomListNode(2)
l3=RandomListNode(3)
l.next=l2
l.random=l3
l2.next=l3
l2.random=l

s=Solution()
print(s.Clone(l))


