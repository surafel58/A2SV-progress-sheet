class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        decStack = []
        minVal = nums[0]

        n = len(nums)

        for i in range(1, n):
            while decStack and decStack[-1][0] <= nums[i]:
                decStack.pop()

            if decStack and decStack[-1][1] < nums[i]:
                return True

            decStack.append((nums[i], minVal))
            minVal = min(minVal, decStack[-1][0])

        return False
