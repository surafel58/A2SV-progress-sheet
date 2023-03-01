class Solution:
    def isPowerOfThree(self, n: int) -> bool:

        value = self.power(n)
        return value

    def power(self, n):
        
        #base case
        if n == 1:
            return n
        
        if n < 1:
            return 0
        
        
        #recurrence relation
        result = self.power(n / 3)

        return result
