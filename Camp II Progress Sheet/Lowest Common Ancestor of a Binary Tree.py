# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        path1 = []
        path2 = []

        def find(node, path, target):

            if node == target:
                path.append(node)
                return True

            path.append(node)

            if node.left:
                if find(node.left, path, target):
                    return True

            if node.right:
                if find(node.right, path, target):
                    return True

            path.pop()
            return False

        find(root, path1, p)
        find(root, path2, q)

        result = []
        i = 0
        
        while i < min(len(path1), len(path2)):
            if path1[i] == path2[i]:
                result.append(path1[i])
            i += 1

        return result[-1]
