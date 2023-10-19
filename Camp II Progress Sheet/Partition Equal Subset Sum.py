class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        

        memo = dict()
        
        def dp(i, targetSum):
            
            if i == len(nums) and targetSum == 0:
                return True

            if i >= len(nums):
                return False

            if (i, targetSum) in memo:
                return memo[(i, targetSum)]

            memo[(i, targetSum)] = dp(i + 1, targetSum - nums[i]) or dp(i + 1, targetSum)
            
            return memo[(i, targetSum)]


        if sum(nums) % 2 != 0:
            return False
            
        return dp(0, sum(nums) // 2)
