# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:

        result = ""

        def buildStr(root):
            # nonlocal result
            if root == None:
                return ""

            result = str(root.val)

            if root.left:
                result += '(' + buildStr(root.left) + ')'

            if not root.left and root.right:
                result += "()"
            
            if root.right:
                result += '(' + buildStr(root.right) + ')'

            return result

        result = buildStr(root)

        return result

