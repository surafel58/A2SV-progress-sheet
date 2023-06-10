# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.memo = dict()

    def rob(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0

        if (root.left == None and root.right == None):
            return root.val

        if root in self.memo:
            return self.memo[root]

        option1 = root.val
        option2 = 0

        if root.left:
            option1 += self.rob(root.left.left)
            option1 += self.rob(root.left.right)

            option2 += self.rob(root.left)

        if root.right:
            option1 += self.rob(root.right.right)
            option1 += self.rob(root.right.left)

            option2 += self.rob(root.right)

        self.memo[root] = max(option1, option2)
        
        return self.memo[root]
