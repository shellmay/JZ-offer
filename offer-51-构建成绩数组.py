class Solution:
    def isMatch(self, s, pattern):
        s, pattern = '#' + s, '#' + pattern
        m, n = len(s), len(pattern)
        dp = [[False] * n for _ in range(m)]
        dp[0][0] = True

        for i in range(m):
            for j in range(1, n):
                if i == 0:
                    dp[i][j] = j > 1 and pattern[j] == '*' and dp[i][j - 2]
                elif pattern[j] in [s[i], '.']:
                    dp[i][j] = dp[i - 1][j - 1]
                elif pattern[j] == '*':
                    dp[i][j] = j > 1 and dp[i][j - 2] or pattern[j - 1] in [s[i], '.'] and dp[i - 1][j]
                else:
                    dp[i][j] = False
        return dp[-1][-1]


