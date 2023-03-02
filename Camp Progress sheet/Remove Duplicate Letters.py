class Solution:
    def removeDuplicateLetters(self, s: str) -> str:

        monoStack = []
        visited = set([])
        to_be_vistied = dict([])

        for i in range(len(s)):
            to_be_vistied[s[i]] = i

        for i in range(len(s)):
            while monoStack and (s[i] not in visited) and monoStack[-1] > s[i]:
                if to_be_vistied[monoStack[-1]] > i:
                    temp = monoStack.pop()
                    visited.remove(temp)
                else:
                    break
            if s[i] not in visited:
                monoStack.append(s[i])
                visited.add(s[i])

        return "".join(monoStack)
