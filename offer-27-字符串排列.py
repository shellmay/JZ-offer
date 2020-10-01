#字符串全排列
class Solution:
    def Permutation(self, ss):
        if not ss: return []
        ss=list(sorted(ss))
        res=[]
        def helper(ss,tmp):
            if not ss: res.append(''.join(tmp))
            for i,char in enumerate(ss):
                if i>0 and ss[i]==ss[i-1]:
                    continue
                helper(ss[:i]+ss[i+1:],tmp+[char])
        helper(ss,[])
        return res
#数组全排列
class Solution2:
    def permuteUnique(self, nums):
        res=[]
        nums.sort()
        def helper(nums,temp):
            if not nums:
                res.append(temp)
            for i in range(len(nums)):
                if i>0 and nums[i]==nums[i-1]:
                    print(nums)
                    continue
                helper(nums[:i]+nums[i+1:],temp+[nums[i]])
        helper(nums,[])
        return res


s=Solution()
end=s.Permutation('aaaaaaa')
print(end)