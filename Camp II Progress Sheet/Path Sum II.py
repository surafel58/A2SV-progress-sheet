# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        solution = []
        def dfs(node, path, amount):

            if not node.left and not node.right:
                path.append(node.val)
                if amount + node.val == targetSum:
                    solution.append(path.copy())
                
                path.pop()
                return

            path.append(node.val)

            if node.left:    
                dfs(node.left, path, amount + node.val)
            
            if node.right:
                dfs(node.right, path, amount + node.val)

            path.pop()
        
        if root != None:
            dfs(root, [], 0)

        return solution
