class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = set()
        def backtrack(index, acc):
            if index >= n:
                return

            if len(acc) == 0 or acc[-1] <= nums[index]:
                
                acc.append(nums[index])

                if len(acc) >= 2 and tuple(acc) not in result:
                    result.add(tuple(acc))
                
                backtrack(index + 1, acc)

                acc.pop()

            backtrack(index + 1, acc)

        backtrack(0, [])

        result = list(result)

        return result
