class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        
        bit_len = max(x.bit_length(), y.bit_length())
        counter = 0
        
        for i in range(bit_len):
            a = 1 & x
            b = 1 & y
            counter += (a ^ b)

            x = x >> 1
            y = y >> 1

        return counter    
