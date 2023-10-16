class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:

        a_set = set(a) 
        
        for char in b:
            if char not in a_set:
                return -1

        #Build LPS
        lps = [0 for _ in range(len(b))]
        n = len(a)
        m = len(b)

        def buildLps():

            prev, curr = 0, 1
            while curr < m:

                if b[prev] == b[curr]:
                    lps[curr] = prev + 1
                    curr += 1
                    prev += 1

                elif prev == 0:
                    curr += 1

                else:
                    prev = lps[prev - 1] 

        buildLps()
        i, j = 0, 0
        result = 1
        isMatched = False

        while True:
            
            if b[j] == a[i]:
                isMatched = True
                j += 1
                i += 1

            elif j == 0:
                i += 1
            
            else:
                j = lps[j - 1]

            if j == m:
                print(i - j)
                return result
            
            #increment result if we go another round
            if i == n:
                result += 1
            
            #check if not char is matched at the end of the string a or char is not found afterall
            if (not isMatched and i == n) or result * n > 10**4:
                return -1 

            i %= n

        return -1
