# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#判断树是都匹配时：
#这道题要清楚终止条件
#1、tree2被匹配完，return True
#2、tree1被匹配完tree2没有匹配完，return False
#3、节点值不同，return False
#返回值：
#左右子树是否匹配
#临界点为两树有一为空，则 return False
#递归时：
#

class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        def issutree(p1,p2):
            #tree2为空说明匹配完毕
            if not p2: 
                return True
            #tree1为空或者值不等说明不匹配
            if not p1 or p1.val != p2.val:
                return False
            return issutree(p1.left,p2.left) and issutree(p1.right,p2.right)
        #匹配一开始两树书否有空的情况，验证当前两数是否匹配，验证tree1左子树是否与tree2匹配，验证tree1右子树是否与tree2匹配，只要找都一个符合条件的即为True，否则为False
        return bool(pRoot1 and pRoot2) and (issutree(pRoot1,pRoot2) or self.HasSubtree(pRoot1.left,pRoot2) or self.HasSubtree(pRoot1.right,pRoot2))
