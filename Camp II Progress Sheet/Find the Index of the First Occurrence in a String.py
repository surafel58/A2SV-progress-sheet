class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        #build LPS
        prev, curr = 0, 1
        lps = [0 for _ in range(len(needle))]

        if len(needle) > len(haystack):
            return -1
        
        while curr < len(needle):

            if needle[prev] == needle[curr]:
                lps[curr] = prev + 1
                curr += 1
                prev += 1

            elif prev == 0:
                curr += 1

            else:
                prev = lps[prev - 1] 


        n_i, h_i = 0, 0

        while h_i < len(haystack):
            
            if needle[n_i] == haystack[h_i]:
                n_i += 1
                h_i += 1

            elif n_i == 0:
                h_i += 1
            
            else:
                n_i = lps[n_i - 1]

            if n_i == len(needle):
                return h_i - n_i

        return -1
