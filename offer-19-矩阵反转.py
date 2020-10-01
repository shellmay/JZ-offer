# -*- coding:utf-8 -*-

class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        res = []
        while matrix:
            res += matrix.pop(0)
            print(matrix)
            matrix = list(zip(*matrix))
            print(matrix)
            matrix=matrix[::-1]
        return res

m=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
s=Solution()
b=s.printMatrix(m)
print(b)