#naive approach
class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        bits = self.generateString(n, k)

        return bits[k-1]

    def generateString(self, n, k):
        if n == 1:
            return "0"

        leftHalf = self.generateString(n-1, k)

        rightHalf = ""
        for i in range(len(leftHalf) - 1, -1, -1):
            if leftHalf[i] == "1":
                rightHalf += "0"
            else:
                rightHalf += "1"

        return leftHalf + "1" + rightHalf

#best way
class Solution:

    def findKth(self, n, k):
        
        if n == 1:
            return 0

        prevLen = (2 ** (n-1)) - 1
        
        if k - (prevLen) == 1:
            return 1

        if k <= (prevLen):
            ans = self.findKth(n-1, k)
        else:
            ans = 1 - self.findKth(n-1, 2 * (prevLen + 1) - k)

        return ans

    def findKthBit(self, n: int, k: int) -> str:
        return str(self.findKth(n,k))

        

