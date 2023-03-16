class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        totalCombination = []
        n = len(candidates)

        def backtrack(index, acc):
            
            # if index >= n:
            #     return

            total = sum(acc)
            if total >= target:
                if total == target:
                    totalCombination.append(acc.copy())
                return 

            for i in range(index, n):
                acc.append(candidates[i])

                backtrack(i, acc)

                acc.pop()

            # backtrack(index + 1, acc)

        backtrack(0, [])

        #O(n^2h)
        return totalCombination



