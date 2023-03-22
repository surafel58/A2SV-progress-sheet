class Solution:
    def maxLength(self, arr: List[str]) -> int:
        n = len(arr)
        maxLen = 0

        def backtrack(index, acc):
            nonlocal maxLen
            if index >= n:
                return

            acc.append(arr[index])
            s = ''.join(acc)
            freq = Counter(s)

            if max(freq.values()) <= 1:
                
                maxLen = max(maxLen, len(s))
                backtrack(index + 1, acc)

            acc.pop()

            backtrack(index + 1, acc)

        backtrack(0, [])

        return maxLen
