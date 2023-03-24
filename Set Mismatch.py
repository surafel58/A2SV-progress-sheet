class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        i = 0
        result = []

        while i < len(nums):
            if nums[i] - 1 != i and nums[nums[i] - 1] != nums[i]:
                temp = nums[i] - 1
                nums[temp], nums[i] = nums[i], nums[temp]
            else:
                i += 1 

        for i in range(len(nums)):
            if nums[i] - 1 != i:
                result.append(nums[i])
                result.append(i + 1)

        return result
