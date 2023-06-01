class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = dict()
        
        def dp(i, isLastSelected):
            if i == 0:
                if isLastSelected:
                    return 0

                return nums[i]

            if i == 1:
                if isLastSelected:
                    return nums[1]

                return max(nums[0], nums[1])
            
            if (i, isLastSelected) in memo:
                return memo[(i, isLastSelected)]
    
            memo[(i, isLastSelected)] =  max(dp(i-1, isLastSelected), nums[i] + dp(i - 2, isLastSelected))

            return memo[(i, isLastSelected)]

        #edge case
        if len(nums) <= 2:
            return max(nums)

        return max(dp(len(nums) - 2, False), nums[-1] + dp(len(nums) - 3, True)) 



            
