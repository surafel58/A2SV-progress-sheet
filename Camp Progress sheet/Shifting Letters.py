class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        
        s = list(s)
        
        prefixSum = [0] * (len(s) + 1)

        for i in range(len(shifts)):
            
            leftIndex = shifts[i][0] 
            rightIndex = shifts[i][1]
            shift = shifts[i][2]

            if shift == 0:
                prefixSum[leftIndex] -= 1
                prefixSum[rightIndex + 1] += 1

            else:
                prefixSum[leftIndex] += 1
                prefixSum[rightIndex + 1] -= 1


        for i in range(1, len(s)):
            prefixSum[i] += prefixSum[i-1]
        
        for i in range(len(s)):
            offset = (ord(s[i]) - 97 + prefixSum[i]) % 26
            s[i] = chr(ord('a') + offset)

        return ''.join(s)
