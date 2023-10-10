# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        prefixSum = defaultdict(int)
        count = 0

        if not root:
            return count 
        
        def buildSum(node, amount):

            if not node.left and not node.right:
                node.val += amount
                return

            node.val += amount

            if node.left:
                buildSum(node.left, node.val)
            
            if node.right:
                buildSum(node.right, node.val)

        buildSum(root, 0)

        def dfs(node):
            nonlocal count
            print(targetSum, node.val)
            
            if not node.left and not node.right:
                if targetSum == node.val:
                    count += 1
                
                count += prefixSum[node.val - targetSum ]
                return

            if targetSum == node.val:
                count += 1
            
            count += prefixSum[node.val - targetSum]
            
            prefixSum[node.val] += 1
            
            if node.left:
                dfs(node.left)

            if node.right:
                dfs(node.right)

            prefixSum[node.val] -= 1
        
        dfs(root)

        return count
        
