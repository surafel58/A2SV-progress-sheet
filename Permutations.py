class Solution:
    def __init__(self):
        self.nums = []
        self.n = 0
        self.result = []
        self.remaningNumber = 0

        
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        self.nums = nums
        self. n = len(nums)
        self.findPermutations([])

        return self.result

    def findPermutations(self, acc): 
        
        if len(acc) == self.n:
            self.result.append(acc.copy())
            return

        for i in range(self.n):
            
            if self.nums[i] not in acc:
                acc.append(self.nums[i])
                self.findPermutations(acc) 

                acc.pop()


