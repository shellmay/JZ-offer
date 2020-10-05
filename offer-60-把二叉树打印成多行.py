# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        resultArray = []
        if not pRoot:
            return resultArray
        curLayerNodes = [pRoot]
        isEvenLayer = True
        while curLayerNodes:
            curLayerValues = []
            nextLayerNodes = []
            isEvenLayer = not isEvenLayer
            for node in curLayerNodes:
                curLayerValues.insert(0, node.val) if isEvenLayer else curLayerValues.append(node.val)
                if node.left:
                    nextLayerNodes.append(node.left)
                if node.right:
                    nextLayerNodes.append(node.right)
            curLayerNodes = nextLayerNodes
            resultArray.append(sorted(curLayerValues))
        return resultArray
    
    # -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#用栈存储一层的结点
import collections
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        if not pRoot:return []
        re=[pRoot]
        result=[]
        while re:
            c=[]
            rec=[]
            for cur in re:
                c.append(cur.val)
                if cur.left:
                    rec.append(cur.left)
                if cur.right:
                    rec.append(cur.right)
            result.append(c)
            re = rec
        return result
