# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if not root:
            return []
        res=[]
        head=root
        qu=[]
        qu.append([head,expectNumber-head.val,[head.val]])
        while qu:
            head,expectNumber,list_node=qu.pop()
            if expectNumber==0 and head.left==None and head.right==None:
                res.append(list_node)
            if head.right:
                qu.append([head.right,expectNumber-head.right.val,list_node+[head.right.val]])
            if head.left:
                qu.append([head.left,expectNumber-head.left.val,list_node+[head.left.val]])

        return res
    #深度优先的算法
    #思想：
    #1、当目标值为0并且为叶子节点走完时，满足条件加入结果中
    #2、深度遍历左右子树发现该路劲
    #3、一次递归完毕时不符合条件要pop出结果，即回溯
    #4、注意深浅拷贝：cur[:]和cur的区别
    def FindPath(self, root, expectNumber):
        res, cur = [], []
        def DFS(root, expectNumber):
            if not root:
                return
            cur.append(root.val)
            expectNumber -= root.val
            if expectNumber == 0 and root.left == None and root.right == None:
                res.append(cur[:])
            DFS(root.left, expectNumber)
            DFS(root.right, expectNumber)
            cur.pop()

        DFS(root,expectNumber)
        return res
