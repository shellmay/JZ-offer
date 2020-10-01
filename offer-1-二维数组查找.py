a=[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here

        for i in range(len(array)):
            if target in array[i]:
                return True
        return False

n=Solution()
end=n.Find(0,a)
print(end)