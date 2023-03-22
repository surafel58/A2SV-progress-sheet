# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.prefixSum = defaultdict(int)
        self.counter = 0
        self.targetSum = 0
        self.nodeSum = 0

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        self.targetSum = targetSum
        self.findPaths(root)
        
        return self.counter

    def findPaths(self, root):

        if root == None:
            return 

        self.nodeSum += root.val


        if self.targetSum == self.nodeSum:
            self.counter += 1

        target = self.nodeSum - self.targetSum

        if target in self.prefixSum:
            self.counter += self.prefixSum[target]

        self.prefixSum[self.nodeSum] += 1
        
        left = self.findPaths(root.left)

        right = self.findPaths(root.right)

        self.prefixSum[self.nodeSum] -= 1

        if self.prefixSum[self.nodeSum] == 0:
            self.prefixSum.pop(self.nodeSum)

        self.nodeSum -= root.val
