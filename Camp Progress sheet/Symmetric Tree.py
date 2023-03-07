# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.checkSymmetric(root.left, root.right)


    def checkSymmetric(self, node1, node2):
            
        if node1 == None and node2 == None:
            return True
        
        elif node1 == None and node2:
            return False

        elif node2 == None and node1:
            return False

        path1 = self.checkSymmetric(node1.left, node2.right)
        path2 = self.checkSymmetric(node1.right, node2.left)

        return path1 and path2 and node1.val == node2.val
