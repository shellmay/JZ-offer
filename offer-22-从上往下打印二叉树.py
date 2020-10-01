# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if not root:
            return []
        res,que=[],collections.deque()
        que.append(root)
        while que:
            tmp=que.popleft()
            res.append(tmp.val)
            if tmp.left:
                que.append(tmp.left)
            if tmp.right:
                que.append(tmp.right)
        return res