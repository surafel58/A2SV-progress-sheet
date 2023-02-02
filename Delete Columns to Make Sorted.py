class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        strLength = len(strs[0])
        counter = 0
        if len(strs) == 1:
            return 0

        for i in range(strLength):
            for j in range(len(strs) - 1):
                if strs[j][i] > strs[j + 1][i]:
                    counter += 1
                    break
        
        return counter
        
