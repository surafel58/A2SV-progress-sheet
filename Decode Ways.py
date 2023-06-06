class Solution:
    def __init__(self):
        self.memo = dict()
    
    def numDecodings(self, s: str) -> int:
        
        return self.dp(s)

    def dp(self, data):
        # Base Case 1: Empty string
        if not data:
            return 1

        first_call, second_call = 0, 0

        if data in self.memo:
            return self.memo[data]

        if 1 <= int(data[:1]) <= 9:
            first_call = self.dp(data[1:])

        if 10 <= int(data[:2]) <= 26:
            second_call = self.dp(data[2:])

        self.memo[data] = first_call + second_call

        return self.memo[data]
