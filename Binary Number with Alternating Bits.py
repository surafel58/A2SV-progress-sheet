class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        prev = 0

        while n != 0:
            #test bit
            test = n & 1
            if test == 0:
                test = -1

            #compare with previous
            if prev == 0:
                prev = test
            elif prev * test == -1:
                prev *= -1
            else:
                return False
            
            n >>= 1
            
        return True
