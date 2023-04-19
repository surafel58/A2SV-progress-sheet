class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = Counter(nums)
        nums = list(set(nums))
        for i in range(len(nums)):
            nums[i] = (freq[nums[i]], nums[i])

        result = []

        def quickSort(left, right):
            #basecase
            if left > right:
                return
    
            pivot = nums[left]
            read, write = left + 1, left + 1

            for read in range(left + 1, right + 1):
                
                if nums[read][0] <= pivot[0]:
                    nums[read], nums[write] = nums[write], nums[read]
                    write += 1

            nums[left], nums[write - 1] = nums[write - 1], nums[left]
            
            if len(nums) - (write - 1) > k:
                quickSort(write, right)

            elif len(nums) - (write - 1) <= k:
                for i in range(right, write - 2, -1):
                    result.append(nums[i][1])
                
                quickSort(left, write - 2) 
            
        quickSort(0, len(nums) - 1)

        return result
