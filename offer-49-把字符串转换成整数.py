class Solution:
    def StrToInt(self, s):
        # write code here
        if not s:
            return 0
        l = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,'+':'+','-':'-'}
        sum = 0
        label = 1
        for i in s:
            if i in l:
                if i == '+':
                    continue
                elif i == '-':
                     label = -1
                else:
                    sum = sum*10 + l[i]
            else:
                return 0
        if -0x80000000 <= sum*label <= 0x7FFFFFFF:
            return sum*label
        else:
            return 0