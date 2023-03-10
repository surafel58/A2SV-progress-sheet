class Solution:
    def __init__(self):
        self.bucket = [0]
        self.minUnfairness = float("inf")
    
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        
        self.bucket = [0] * k
        
        #??
        cookies.reverse()
        
        self.backtrack(0, len(cookies), cookies)
        
        return self.minUnfairness

    def backtrack(self, index, n, cookies):

        if index >= n:
            self.minUnfairness = min(self.minUnfairness, max(self.bucket))
            return

        if max(self.bucket) >= self.minUnfairness:# pruning case and > or >= have no difference
            return

        for i in range(len(self.bucket)):
            self.bucket[i] += cookies[index]
            
            self.backtrack(index + 1, n, cookies)

            self.bucket[i] -= cookies[index]
