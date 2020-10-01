class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        return s.replace(' ','%20')
l='sd sd sd'
n=Solution()
end=n.replaceSpace(l)
print(end)




