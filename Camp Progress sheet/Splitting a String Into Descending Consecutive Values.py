class Solution:
    def splitString(self, s: str) -> bool:
        current = []

        def backtrack(index):

            if index >= len(s):
                return len(current) >= 2


            for i in range(index, len(s)):
                nextCandidate = int(s[index:i + 1])

                if len(current) == 0 or current[-1] - nextCandidate == 1:
                    current.append(nextCandidate)

                    if backtrack(i + 1):
                        return True

                    current.pop()
            
            return False

        return backtrack(0)
