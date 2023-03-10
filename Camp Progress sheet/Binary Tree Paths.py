# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.paths = []
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.findPaths(root, [])
        return self.paths

    def findPaths(self, root, path):
        if root == None:
            path.append("")
            return
        
        if root.left == None and root.right == None:
            path.append(str(root.val))
            self.paths.append("->".join(path))
            return 


        path.append(str(root.val))
        self.findPaths(root.left, path)
        path.pop()


        self.findPaths(root.right, path)
        path.pop()
        
