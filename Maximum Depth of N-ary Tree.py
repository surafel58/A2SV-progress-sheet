"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        
        maxDepth = 0
        visited = set()

        def dfs(node, visited, depth):
            nonlocal maxDepth

            if not node.children:
                maxDepth = max(maxDepth, depth)
                return

            visited.add(node)

            for neighbour in node.children:
                if neighbour not in visited:
                    traerse = dfs(neighbour, visited, depth + 1)

        
        
        if not root:
            return maxDepth

        dfs(root, set(), 1)
        return maxDepth

            
