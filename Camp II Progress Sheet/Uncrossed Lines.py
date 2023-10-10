class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        
        memo = dict()
        def dp(i, j):

            if i >= len(nums1) or j >= len(nums2):
                return 0

            if (i, j) in memo:
                return memo[(i, j)]

            ans1 = 0
            ans2 = 0
            ans3 = 0

            if nums1[i] == nums2[j]:
                ans1 = max(ans1, 1 + dp(i + 1, j + 1)) 
            
            else:
                ans2 = max(ans2, dp(i, j + 1))
                ans3 = max(ans3, dp(i + 1, j))

            memo[(i, j)] = max(max(ans1, ans2), ans3)

            return memo[(i, j)]

        return dp(0, 0)
