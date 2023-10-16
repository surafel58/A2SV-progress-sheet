# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        
        seen = set()
        result = []
        temp = dict()

        def dfs(node):

            if not node:
                return []

            left = dfs(node.left)
            right = dfs(node.right)
            subtree = None
            
            if left and right:
                subtree = [tuple(left + [node.val] + right), "both"]
            
            elif left:
                subtree = [tuple(left + [node.val] + right), "left"]
            
            elif right:
                subtree = [tuple(left + [node.val] + right), "right"]
            
            else:
                subtree = [tuple(left + [node.val] + right), "leaf"]

            if tuple(subtree) in seen:
                temp[tuple(subtree)] = node

            seen.add(tuple(subtree))
            return subtree

        dfs(root)
        
        for key in temp:
            result.append(temp[key])
        
        return result

        
