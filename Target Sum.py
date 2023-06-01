class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = dict()

        def findWays(amount, i):

            if i >= len(nums):
                if amount == target:
                    return 1
                return 0

            if (amount, i) in memo:
                return memo[(amount, i)]

            k = findWays(amount + nums[i], i + 1) + findWays(amount - nums[i], i + 1)

            memo[(amount, i)] = k

            return k

        return findWays(0, 0)
