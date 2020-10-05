#全部遍历
class Solution:
    def KthNode(self, pRoot, k):
        res = []
        rsnode=[]
        if k <=0:
            return None
        def dfs(pRoot, res):
            if not pRoot:
                return
            dfs(pRoot.left, res)
            res.append(pRoot.val)
            rsnode.append(pRoot)
            dfs(pRoot.right, res)

        dfs(pRoot, res)
        if len(res)<k:
            return None
        for i in rsnode:
            if i.val==res[k-1]:
                return i
#中序遍历
class Solution:
    count = 0
    def KthNode(self, pRoot, k):
        if not pRoot:
            return None
        node = self.KthNode(pRoot.left, k)
        if node:
            return node
        self.count += 1
        if self.count == k:
            return pRoot
        node = self.KthNode(pRoot.right, k)
        if node:
            return node



