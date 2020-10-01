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



