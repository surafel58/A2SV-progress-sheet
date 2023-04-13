# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:

        result = 0

        def findSum(root):
            nonlocal result

            if root == None:
                return

            #check if node is even
            if root.val % 2 == 0:

                #check if it has child or grand child
                if root.left:
                    if root.left.left:
                        result += root.left.left.val 
                    if root.left.right:
                        result += root.left.right.val
                
                #check if it has child or grand child
                if root.right:
                    if root.right.left:
                        result += root.right.left.val 
                    if root.right.right:
                        result += root.right.right.val

            left = findSum(root.left)
            right = findSum(root.right)
        
        findSum(root)
        
        return result
