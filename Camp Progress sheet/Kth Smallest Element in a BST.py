# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        counter = 0
        kth_num = 0

        def findK(root):
            nonlocal counter
            nonlocal kth_num

            if root:
                
                left = findK(root.left)

                counter += 1
                if counter == k:
                    kth_num = root.val

                right = findK(root.right)

        findK(root)

        return kth_num
