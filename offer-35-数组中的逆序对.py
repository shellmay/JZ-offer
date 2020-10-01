# -*- coding:utf-8 -*-
class Solution:
    def InversePairs(self, data):
        n = len(data)
        if n <= 1:
            return 0
        mid = n // 2
        left = data[:mid]
        right = data[mid:]
        result = self.InversePairs(left) + self.InversePairs(right)

        # union left and right
        left.sort()
        right.sort()
        index = 0
        for j in range(len(right)):
            while index < len(left) and left[index] <= right[j]:
                index += 1
            result += (len(left) - index)
        return result
data=[1,2,3,4,5,6,7,0]
s=Solution()
end=s.InversePairs(data)
print(end)