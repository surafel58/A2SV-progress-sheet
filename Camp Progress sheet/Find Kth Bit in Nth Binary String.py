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


        
             
