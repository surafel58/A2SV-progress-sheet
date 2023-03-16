class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        totalCombination = set()
        n = len(candidates)
        candidates.sort()

        if sum(candidates) < target:
            return []
        
        def backtrack(index, acc):
            nonlocal target

            if target <= 0:
                if target == 0:
                    totalCombination.add(tuple(acc))
                return            

            if index >= n:
                return

                
            acc.append(candidates[index])
            target -= candidates[index]
            
            backtrack(index + 1, acc)
            
            target += candidates[index]
            acc.pop()

            #jump duplicate numbers, since we already visited the possiblity, it will be repeated
            while index + 1 < len(candidates) and candidates[index] == candidates[index + 1]:
                index += 1

            backtrack(index + 1, acc)

        backtrack(0, [])

        #O(2^depth)
        return totalCombination
