class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:

        nums.sort()
        nums[0] += k

        for i in range(1, len(nums)):
            if -k <= nums[i - 1] - nums[i] <= k:
                nums[i] += (nums[i - 1] - nums[i])
            else:
                nums[i] += -k

        return max(nums) - min(nums)
