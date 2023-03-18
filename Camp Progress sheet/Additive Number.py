class Solution:
    def __init__(self):
        self.num = ""
        self.n = 0
    
    def isAdditiveNumber(self, num: str) -> bool:
        
        self.num = num
        self.n = len(num)
        
        return self.checkSequence(0, [])

    def checkSequence(self, index, acc):
        
        if index >= self.n:
            return len(acc) > 2

        for i in range(index, self.n):

            currentVal = self.num[index:i+1]
            
            #edge case. when sequence contains 0(but the substring length must be more than 1)
            if len(currentVal) > 1 and currentVal[0] == "0":
                continue

            currentVal = int(currentVal)

            if len(acc) < 2 or acc[-1] + acc[-2] == currentVal:
                acc.append(currentVal)
                
                if self.checkSequence(i + 1, acc):
                    return True

                acc.pop()

        return False

        
