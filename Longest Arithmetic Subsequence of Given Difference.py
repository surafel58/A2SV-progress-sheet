import collections
class Solution(object):
    def longestSubsequence(self, arr, diff):
        dp = collections.Counter()
        for a in arr:
            dp[a] = max(dp[a], dp[a - diff] + 1)
        return max(dp.values())
