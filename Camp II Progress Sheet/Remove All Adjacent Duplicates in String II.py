class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:

        stack = []
        result = []

        for char in s:
            if stack and stack[-1][1] == k:
                stack.pop()

            if stack and stack[-1][0] == char:
                temp = stack.pop()
                stack.append((temp[0], temp[1] + 1))
            else:
                stack.append((char, 1))

        else:
            if stack and stack[-1][1] == k:
                stack.pop()

        while stack:
            temp = stack.pop()

            for i in range(temp[1]):
                result.append(temp[0])

        return "".join(result[::-1])
