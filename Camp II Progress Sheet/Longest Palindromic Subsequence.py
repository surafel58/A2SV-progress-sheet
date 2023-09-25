class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        memo = dict()

        def dp(i, j):
            print(i, j)
            if i == j:
                return 1

            if i > j:
                return 0

            if (i, j) in memo:
                return memo[(i, j)]
            
            ans = 0
            if s[i] == s[j]:
                ans = 2 + dp(i + 1, j - 1)
            else:
                ans = max(dp(i + 1, j), dp(i, j - 1))
            
            memo[(i, j)] = ans
            
            return memo[(i, j)]

        return dp(0, len(s) - 1)
