class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if not pRoot:
            return 0
        return 1+max(self.TreeDepth(pRoot.left),self.TreeDepth(pRoot.right))
