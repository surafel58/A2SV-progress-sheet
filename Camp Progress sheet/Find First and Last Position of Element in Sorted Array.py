class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.searchLeftIndex(nums, target)
        right = self.searchRightIndex(nums,target)
        result = [left, right]

        return result

    def searchLeftIndex(self, nums, target):
        left = 0
        right = len(nums) - 1
        value = -1

        while left <= right:
            mid = left + (right - left) // 2

            if target <= nums[mid]:
                value = nums[mid]
                right = mid - 1
            else:
                left = mid + 1
        
        if value == target:
            return left

        return -1
    
    def searchRightIndex(self, nums, target):
        left = 0
        right = len(nums) - 1
        value = -1

        while left <= right:
            mid = left + (right - left) // 2

            if target >= nums[mid]:
                value = nums[mid]
                left = mid + 1
            else:
                right = mid - 1

        if value == target:
            return right
        return -1
