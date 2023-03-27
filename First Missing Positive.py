class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] - 1 != i and 0 < nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                temp = nums[i] - 1
                nums[i], nums[temp] = nums[temp], nums[i]
            else:
                i += 1 
        
        for i in range(n):
            if nums[i] != (i + 1):
                return (i + 1)
        
        return (n + 1)
