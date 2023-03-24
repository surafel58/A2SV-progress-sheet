class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0

        while i < len(nums):
            if nums[i] - 1 != i and nums[nums[i] - 1] != nums[i]:
                temp = nums[i] - 1
                nums[temp], nums[i] = nums[i], nums[temp]
            else:
                i += 1 

        for i in range(len(nums)):
            if nums[i] - 1 != i:
                return nums[i]

        return 0
