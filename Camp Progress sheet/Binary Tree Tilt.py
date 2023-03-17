# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.result = []
    
    def findTilt(self, root: Optional[TreeNode]) -> int:
        
        self.findTilts(root)

        return sum(self.result)

    def findTilts(self, root):

        if root == None:
            return 0

        left = self.findTilts(root.left)
        right = self.findTilts(root.right)

        self.result.append(abs(left - right))

        return left + right + root.val
