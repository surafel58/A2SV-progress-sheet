class Solution:
    def __init__(self):
        self.arr = []

    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0

        self.arr = [0] * (n + 1)
        self.arr[1] = 1
        
        self.getList(n)
        print(self.arr)

        return max(self.arr)

    def getList(self, i):
        if i <= 1:
            return i
        
        if self.arr[i] != 0:
            return self.arr[i]

        if i % 2 == 0:
            self.arr[i] = self.getList(i // 2)
        else:
            self.arr[i] = self.getList(i // 2) + self.getList((i // 2) + 1)

        self.getList(i - 1)
        
        return self.arr[i]
