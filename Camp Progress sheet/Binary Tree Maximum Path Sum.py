# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max = float("-inf")

    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        self.findMaxSum(root)

        return self.max

    def findMaxSum(self, root):
        if root == None:
            return 0

        left = self.findMaxSum(root.left)
        right = self.findMaxSum(root.right)

        leftPathSum = left + root.val
        rightPathSum = right + root.val
        closedPathSum = left + right + root.val

        self.max = max(self.max, leftPathSum, rightPathSum, closedPathSum, root.val)

        return max(leftPathSum, rightPathSum, root.val)
