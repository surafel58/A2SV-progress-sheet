class Solution:
    def __init__(self):
        self.result = []

    def countSmaller(self, nums: List[int]) -> List[int]:
        self.result = [0] * len(nums)

        num_tuples = []

        #store num - index tuple
        for i in range(len(nums)):
            num_tuples.append((nums[i], i))

        self.mergeSort(num_tuples, 0, len(num_tuples) - 1)
        
        return self.result


    def mergeSort(self, nums, start, end):
        if start == end:
            return [nums[start]]

        mid = start + (end - start) // 2

        left = self.mergeSort(nums, start, mid)
        right = self.mergeSort(nums, mid + 1, end) 

        pointer = 0

        for i in range(len(left)):
            while pointer < len(right) and left[i][0] > right[pointer][0]:
                pointer += 1

            self.result[left[i][1]] += pointer 


        p1 = 0
        p2 = 0
        merged = []

        while p1 < len(left) and p2 < len(right):
            if left[p1][0] <= right[p2][0]:
                merged.append(left[p1])
                p1 += 1

            else:
                merged.append(right[p2])
                p2 += 1

        merged.extend(left[p1:])
        merged.extend(right[p2:])
        
        return merged
