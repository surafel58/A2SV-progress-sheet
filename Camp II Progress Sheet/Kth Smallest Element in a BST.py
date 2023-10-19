# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        solution = 0

        def dfs(node):
            nonlocal k, solution

            if not node:
                return

            if node.left:
                dfs(node.left)
            
            if k == 1:
                solution = node.val

            k -= 1

            if node.right:
                dfs(node.right)
            
            return

        dfs(root)

        return solution

            
        
