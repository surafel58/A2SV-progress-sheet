# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        
        counter = 0


        def calculateAvg(root):
            
            nonlocal counter

            if root == None:
                return (0,0)

            left = calculateAvg(root.left)
            right = calculateAvg(root.right)

            amount =  left[0] + right[0] + 1
            sum = left[1] + right[1] + root.val

            avg = sum // amount
            
            if avg == root.val:
                counter += 1
            
        
            return (amount, sum)

        calculateAvg(root)
        
        return counter
