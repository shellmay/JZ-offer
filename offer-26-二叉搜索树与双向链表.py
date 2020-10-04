#由于二叉树的中序遍历为有序的数组，座椅根据中序遍历转换二叉树节点为双向链表

class Solution:
    def __init__(self):
        self.listHead = None
        self.listTail = None
    def Convert(self, pRootOfTree):
        if pRootOfTree==None:
            return
        self.Convert(pRootOfTree.left)
        if self.listHead==None:
            self.listHead,self.listTail = pRootOfTree,pRootOfTree
        else:
            self.listTail.right,pRootOfTree.left = pRootOfTree,self.listTail
            self.listTail = pRootOfTree
        self.Convert(pRootOfTree.right)
        return self.listHead
