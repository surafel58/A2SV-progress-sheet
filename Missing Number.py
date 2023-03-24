class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] != i and nums[i] < n:
                temp = nums[i]
                nums[i], nums[temp] = nums[temp], nums[i]
            else:
                
        for i in range(n):
            if nums[i] != i:
                return i
        
        return len(nums)
