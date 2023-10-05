
class Trie:

    def __init__(self):

        self.root = [None, None] # trie = [None, None]
        

    def insert(self, num) -> None:

        curr = self.root

        for shift in range(31, -1, -1): 
            bit = 1 if num & (1 << shift) else 0 # check current bit at shift position
            if not curr[bit]:
                curr[bit] = [None, None]

            curr = curr[bit]
            

    def search(self, num):
        
        curr = self.root

        result = []

        for shift in range(31, -1, -1): 
            bit = 1 if num & (1 << shift) else 0
            if bit:
                if curr[0]:
                    result.append("0")
                    curr = curr[0]
                else:
                    result.append("1")
                    curr = curr[1]

            else:
                if curr[1]:
                    result.append("1")
                    curr = curr[1]

                else:
                    result.append("0")
                    curr = curr[0]

        return int("".join(result) , 2) ^ num

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        maxResult = 0
        trie = Trie()

        for num in nums:
            trie.insert(num)
            temp = trie.search(num)
            maxResult = max(maxResult, temp)

        return maxResult
