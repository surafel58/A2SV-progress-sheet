class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        # if len(nums) == 1:
        #     return nums[0]
        
        # if k == len(nums) == k:
        #3,2,1,5,6,4
        #1,2,3,4,5,6
        result = 0

        def quickSort(left, right):
            nonlocal result

            # if right <= left:
            #     return

            # pivots = [left, (left + right) // 2, right]
            # pivots.sort(key = lambda a : nums[a])
            # nums[left], nums[pivots[1]] = nums[pivots[1]], nums[left]
            pivot = nums[left]
            read, write = left + 1, left + 1 

            for read in range(left + 1, right + 1):
                if nums[read] <= pivot:
                    nums[read], nums[write] = nums[write], nums[read]
                    write += 1

            nums[left], nums[write - 1] = nums[write - 1], nums[left]

            if len(nums) - (write - 1) == k:
                result = nums[write - 1]
                return

            elif len(nums) - (write - 1) < k:
                quickSort(left, write - 2) 
            else:
                quickSort(write, right)
        
        quickSort(0, len(nums) - 1)
        return result
    
