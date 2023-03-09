class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def backtrack(i, acc):
            #base case
            if len(acc) == k:
                ans.append(acc[:]) #copy it instead of passing the variable(since it is pass by reference)
                return 

            #dead end
            if i > n:   
                return 

            # for(i in range(i, n + 1):
            
            #insert candidate or option
            acc.append(i)
            backtrack(i + 1, acc)
            
            #no insert option
            acc.pop()
            backtrack(i + 1, acc)

        backtrack(1, [])

        return ans
