class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = dict()
        
        def dp(i, amount):
            count = 0

            if amount < 0:
                return 0

            if amount == 0:
                return 1

            if (i, amount) in memo:
                return memo[(i, amount)]

            for index in range(len(nums)):
                count += dp(index, amount - nums[index]) 
           
            memo[(i,amount)] = count

            return memo[(i, amount)]

        return dp(0, target)
                
