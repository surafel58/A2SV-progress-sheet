class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        lettersMaxindex = defaultdict(int)

        for i in range(len(s)):
             lettersMaxindex[s[i]] = i

        i = 0
        maxIndex = 0 
        start = -1
        partitions = []
        while i < len(s):
            maxIndex = max(maxIndex, lettersMaxindex[s[i]]) 
            if i == maxIndex:
                partitions.append(maxIndex - start)
                maxIndex = i
                start = maxIndex
            i += 1
        return partitions
