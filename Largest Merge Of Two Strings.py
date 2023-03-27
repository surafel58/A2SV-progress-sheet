class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        p1 = 0
        p2 = 0

        n = len(word1)
        m = len(word2)
        result = ""

        while p1 < n and p2 < m:
            if word1[p1:] >= word2[p2:]:
                result += word1[p1]
                p1 += 1
            else:
                result += word2[p2]
                p2 += 1

        result += word1[p1:]
        result += word2[p2:]
        
        return result
