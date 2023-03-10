class Solution:
    def __init__(self):
        self.solution = []

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.findAllSubSets(0, [], nums, len(nums))
        self.solution.append([])
        return self.solution

    def findAllSubSets(self, index, acc, nums, n):
        if index >= n:
            return 

        for i in range(index, n):
            acc.append(nums[i])
            self.solution.append(acc.copy())

            self.findAllSubSets(i + 1, acc, nums, n)
            acc.pop()
