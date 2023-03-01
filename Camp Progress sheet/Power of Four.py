class Solution:
    def isPowerOfFour(self, n: int) -> bool:

        value = self.power(n)
        return value

    def power(self, n):
        
        #base case
        if n == 1:
            return n
        
        if n % 4 != 0 or n <= 0:
            return 0
        
        
        #recurrence relation
        result = 4 * self.power(n // 4)

        return result
