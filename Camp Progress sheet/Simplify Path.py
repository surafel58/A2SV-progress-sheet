class Solution:
    def simplifyPath(self, path: str) -> str:

        path = path.split("/")

        stack = []

        for i in range(len(path)):
            if path[i] == ".." and stack:
                stack.pop()

            elif path[i] != ".." and path[i] != "." and path[i] != "":
                stack.append(path[i]) 

        result = "/".join(stack)
        result = "/" + result

        return result
