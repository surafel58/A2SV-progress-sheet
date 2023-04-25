class Solution:
    def __init__(self):
        self.nums = []
        self.n = 0
        self.or_subsets = set()   

    def countMaxOrSubsets(self, nums: List[int]) -> int:
        self.nums = nums
        self.n = len(nums)
        self.findSubsets(0, set())

        xorValues = defaultdict(int)
        for subset in self.or_subsets:
            tempXor = 0
            for val in subset:
                tempXor |= nums[val]
            
            xorValues[tempXor] += 1
        
        maxXor = max(xorValues)
        return xorValues[maxXor]

    def findSubsets(self, index, acc):

        for i in range(index, self.n):

            if i not in acc:
                acc.add(i)
                if acc not in self.or_subsets:
                    self.or_subsets.add(tuple(acc))

                self.findSubsets(i + 1, acc) 
                acc.remove(i)
