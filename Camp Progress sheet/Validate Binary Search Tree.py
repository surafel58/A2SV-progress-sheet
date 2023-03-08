# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkValidity(self, root):
        if root == None:
            return (True, [])

        left = self.checkValidity(root.left)

        isLeftValid = True
        isRightValid = True

        for i in range(len(left[1])):
            if left[1][i] >= root.val: 
                isLeftValid = False
                break
        
        right = self.checkValidity(root.right)

        for i in range(len(right[1])):
            if right[1][i] <= root.val: 
                isRightValid = False
                break

        isValid = isLeftValid and isRightValid and left[0] and right[0]
        
        return (isValid, left[1] + [root.val] + right[1])


    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.checkValidity(root)[0]
            
