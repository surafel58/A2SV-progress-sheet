class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        value = nums[0]

        if len(nums) == 1:
            return 1

        for i in range(1,len(nums)):
            if nums[i] == value:
                nums[i] = -101

            else:
                value = nums[i]

        holder = 0
        seeker = 0

        while seeker < len(nums):
            if nums[holder] != -101:
                holder += 1

            elif nums[seeker] != -101:
                nums[holder], nums[seeker] = nums[seeker], nums[holder]
                holder += 1
                
            seeker += 1

        i = 0
        while i < len(nums) and nums[i] != -101:
            i += 1

        return i 

        
