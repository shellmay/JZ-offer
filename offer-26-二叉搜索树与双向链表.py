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
            #值得注意的是，上一个结点的右子树指向当前结点，当前结点的左子树指向前一个结点。
            #因为当前子树的右节点还存在的时候如果改变指向会丢失结点信息
            self.listTail.right,pRootOfTree.left = pRootOfTree,self.listTail
            self.listTail = pRootOfTree
        self.Convert(pRootOfTree.right)
        return self.listHead
