class Solution:
    def longestPrefix(self, s: str) -> str:

        #build LPS
        prev, curr = 0, 1
        lps = [0 for _ in range(len(s))]

        
        while curr < len(s):

            if s[prev] == s[curr]:
                lps[curr] = prev + 1
                curr += 1
                prev += 1

            elif prev == 0:
                curr += 1

            else:
                prev = lps[prev - 1] 

        s = s[::-1]
        temp = lps[-1]
        result = s[0 : temp]
        return result[::-1]
