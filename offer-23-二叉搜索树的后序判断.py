# -*- coding:utf-8 -*-
#二叉搜索树特点：结点的左子树都比根小，结点的右子树都比根大，后序遍历则为左右中，最后一个为根节点
#解题思路：
#找出第一个比根节点大的数，划分左右子树，由于前面已经判断左子树大小，所以接下来判断右子树是否都比根节点大即可。递归实现整个树的判断。
class Solution:
    def VerifySquenceOfBST(self, sequence):
        if sequence is None or len(sequence)==0:
            return False
        n=len(sequence)
        num=sequence[-1]
        i=0
        for i in range(n):
            if sequence[i]>num:
                break
        for j in range(i,n):
            if sequence[j]<num:
                return False
        left=True
        if i >0:
            left=self.VerifySquenceOfBST(sequence[:i])
        right=True
        if i<n-1:
            right=self.VerifySquenceOfBST(sequence[i:-1])
        return left and right

a=[1,6,3,2,5]
s=Solution()
print(s.VerifySquenceOfBST(a))
