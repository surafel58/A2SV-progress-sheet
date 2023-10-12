# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.moves = 0
        def calcMoves(root):
            if not root:
                return 0
            
            left = calcMoves(root.left)
            right = calcMoves(root.right)

            excess = root.val + left + right - 1
            self.moves += abs(excess)

            return excess
        
        calcMoves(root)

        return self.moves
