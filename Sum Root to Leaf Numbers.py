# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        result = 0

        def sumPaths(root, num):
            nonlocal result

            if root.left != None:
                sumPaths(root.left, num + str(root.left.val))
            
            # else:
            #     result += int(num)
            #     return

            if root.right != None:
                sumPaths(root.right, num + str(root.right.val))
            
            elif root.left == None and root.right == None:
                result += int(num)
                return

        sumPaths(root, str(root.val))

        return result
