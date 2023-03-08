class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def traverse(curr):
            
            if not curr:
                return None

            if curr == p or curr == q:
                return curr

            left = traverse(curr.left)
            right = traverse(curr.right)
            

            if left and right:
                return curr

            if left:
                return left

            return right
        
        return traverse(root)
